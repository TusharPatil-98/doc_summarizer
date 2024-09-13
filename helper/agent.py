import os
from haystack import Pipeline

from helper.configurations import ModelConfig
from haystack.components.embedders import HuggingFaceAPITextEmbedder
from haystack.components.builders import PromptBuilder
from haystack.components.generators import HuggingFaceAPIGenerator
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
from haystack.components.readers import ExtractiveReader


class Agent:
    def __init__(self, doc_store) -> None:
        self.__doc_store = doc_store
        self.__pipeline = Pipeline()
        self.__template = """
You are a knowledgable scientist. You run in a loop of Context, Question, Answer.
Context provides you the supporting knowledge required to Answer user Question.
You help users by answering questions related to given document.
You can answer all the related to a given document. 
But you will not add any facts or new knowledge in your answer that is not mentioned in the given document.

Always answer the question based on the given Context.
You will wait for user to ask question before answering.

Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{ query }}
Answer: 
"""
        self.add_components()
        self.connect_components()


    def add_components(self) -> None:
        self.__pipeline.add_component("embedder", HuggingFaceAPITextEmbedder(api_type="serverless_inference_api",
                                                                             api_params={"model": ModelConfig.document_model},
                                                                             token=ModelConfig.hf_token))
        
        self.__pipeline.add_component("prompt_builder", PromptBuilder(template=self.__template))
        self.__pipeline.add_component("llm",
                                      HuggingFaceAPIGenerator(api_type=ModelConfig.api_type,
                                                              api_params={"model": ModelConfig.answer_model}),
                                      )
        
        self.__pipeline.add_component("retriever", InMemoryEmbeddingRetriever(document_store=self.__doc_store))
        
    def connect_components(self) -> None:
        self.__pipeline.connect("embedder.embedding", "retriever.query_embedding")
        self.__pipeline.connect("retriever", "prompt_builder.documents")
        self.__pipeline.connect("prompt_builder", "llm")

    def execute(self, query):
        results = self.__pipeline.run(data={
            "embedder": {"text": query}, 
            "prompt_builder": {"query": query},
            "llm": {"generation_kwargs": {"max_new_tokens": 150}}
            })

        return results['llm']['replies'][0]

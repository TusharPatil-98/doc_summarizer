from haystack import Pipeline

from typing import List, AnyStr
from helper.configurations import ModelConfig, DocumentConfig
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.converters import MarkdownToDocument, PyPDFToDocument, TextFileToDocument

from haystack.components.routers import FileTypeRouter
from haystack.components.joiners import DocumentJoiner

from haystack.components.preprocessors import DocumentCleaner
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.writers import DocumentWriter
from haystack.components.embedders import HuggingFaceAPIDocumentEmbedder

class DocumentStorage:
    def __init__(self) -> None:
        self.__doc_store = InMemoryDocumentStore()
        self.__pipeline = Pipeline()

        self.add_components()
        self.connect_components()
    
    def add_components(self) -> None:

        self.__pipeline.add_component("file_type_router", FileTypeRouter(mime_types=DocumentConfig.supported_mime_types))
        self.__pipeline.add_component("text_file_converter", TextFileToDocument())
        self.__pipeline.add_component("markdown_converter", MarkdownToDocument())
        self.__pipeline.add_component("pypdf_converter", PyPDFToDocument())
        self.__pipeline.add_component("document_joiner", DocumentJoiner())

        self.__pipeline.add_component("cleaner", DocumentCleaner())
        self.__pipeline.add_component("splitter", DocumentSplitter(split_by=DocumentConfig.split_by,
                                                                   split_length=DocumentConfig.split_length,
                                                                   split_overlap=DocumentConfig.split_overlap))
        
        self.__pipeline.add_component("embedder", HuggingFaceAPIDocumentEmbedder(api_type=ModelConfig.api_type,
                                                                                 api_params={"model": ModelConfig.document_model},
                                                                                 token=ModelConfig.hf_token))
        
        self.__pipeline.add_component("writer", DocumentWriter(document_store=self.__doc_store))

    def connect_components(self) -> None:
        self.__pipeline.connect("file_type_router.text/plain", "text_file_converter.sources")
        self.__pipeline.connect("file_type_router.application/pdf", "pypdf_converter.sources")
        self.__pipeline.connect("file_type_router.text/markdown", "markdown_converter.sources")
        self.__pipeline.connect("text_file_converter", "document_joiner")
        self.__pipeline.connect("pypdf_converter", "document_joiner")
        self.__pipeline.connect("markdown_converter", "document_joiner")
        self.__pipeline.connect("document_joiner", "cleaner")
        self.__pipeline.connect("cleaner", "splitter")
        self.__pipeline.connect("splitter", "embedder")
        self.__pipeline.connect("embedder", "writer")

    def execute(self, source: List[AnyStr]) -> None:
        self.__pipeline.run({"file_type_router": {"sources": source}})

    def get_document_store(self):
        return self.__doc_store

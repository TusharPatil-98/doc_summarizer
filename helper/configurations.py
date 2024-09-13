import os
from typing import List
from haystack.utils import Secret
from dataclasses import dataclass


@dataclass
class ModelConfig:
    document_model: str = "sentence-transformers/multi-qa-mpnet-base-dot-v1"
    answer_model: str = "HuggingFaceH4/zephyr-7b-beta"
    api_type: str = "serverless_inference_api"
    hf_token: Secret = Secret.from_token(os.environ["HF_TOKEN"])


class DocumentConfig:
    supported_mime_types: List = ["text/plain", "application/pdf", "text/markdown"]
    split_by: str = "word"
    split_length: int = 150
    split_overlap: int = 50

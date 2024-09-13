import os
from haystack.utils import Secret
from dataclasses import dataclass

@dataclass
class ModelConfig:
    document_model = "sentence-transformers/multi-qa-mpnet-base-dot-v1"
    answer_model = "HuggingFaceH4/zephyr-7b-beta"
    api_type="serverless_inference_api"
    hf_token = Secret.from_token(os.environ["HF_TOKEN"])


class DocumentConfig:
    supported_mime_types = ["text/plain", "application/pdf", "text/markdown"]
    split_by = "word"
    split_length = 150
    split_overlap = 50
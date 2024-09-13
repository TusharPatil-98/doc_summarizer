from typing import AnyStr, List
from helper.configurations import ModelConfig, DocumentConfig
from haystack.utils import Secret


def test_model_config() -> None:
    assert hasattr(ModelConfig, "answer_model")
    assert hasattr(ModelConfig, "api_type")
    assert hasattr(ModelConfig, "document_model")
    assert hasattr(ModelConfig, "hf_token")
    
    mc = ModelConfig()

    assert isinstance(mc.answer_model, str)
    assert isinstance(mc.api_type, str)
    assert isinstance(mc.document_model, str)
    assert isinstance(mc.hf_token, Secret)
    

def test_document_config() -> None:
    supported_mime_types: List = ["text/plain", "application/pdf", "text/markdown"]
    split_by: str = "word"
    split_length: int = 150
    split_overlap: int = 50
    assert hasattr(DocumentConfig, "supported_mime_types")
    assert hasattr(DocumentConfig, "split_by")
    assert hasattr(DocumentConfig, "split_length")
    assert hasattr(DocumentConfig, "split_overlap")
    
    dc = DocumentConfig()

    assert isinstance(dc.supported_mime_types, List)
    assert isinstance(dc.split_by, str)
    assert isinstance(dc.split_length, int)
    assert isinstance(dc.split_overlap, int)

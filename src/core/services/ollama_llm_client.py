from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from src.core.interfaces.llm_client import LLMClient

class OllamaLLMClient(LLMClient):
    def __init__(self, model_name: str, timeout: float = 180.0):
        self.model_name = model_name
        self.timeout = timeout
        self.llm = Ollama(model=model_name, temperature=0, request_timeout=timeout)
        self.embedding = OllamaEmbedding(model_name=model_name, request_timeout=timeout)

    def query(self, prompt: str) -> str:
        response = self.llm.complete(prompt)
        return response.text

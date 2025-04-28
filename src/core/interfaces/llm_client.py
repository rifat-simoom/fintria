from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def query(self, prompt: str) -> str:
        pass

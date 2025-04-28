from abc import ABC, abstractmethod

class ChatbotService(ABC):
    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def chat(self, message: str) -> str:
        pass

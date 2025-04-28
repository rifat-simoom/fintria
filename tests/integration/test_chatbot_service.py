from src.core.services.banking_chatbot_service import BankingChatbotService
from src.core.interfaces.document_loader import DocumentLoader
from src.core.interfaces.llm_client import LLMClient


# Dummy for LLM inner client
class FakeInnerLLM:
    def complete(self, prompt):
        class Response:
            text = "Dummy LLM complete response"
        return Response()

# Dummy for LLMClient interface
class DummyLLM(LLMClient):
    def __init__(self):
        self.llm = FakeInnerLLM()  # 👈 Important: llm attribute needed

    def query(self, prompt: str) -> str:
        return "Dummy response"

# Dummy for document loader
class DummyLoader(DocumentLoader):
    def load_documents(self):
        class DummyDocument:
            text = "Dummy banking document content."
        return [DummyDocument()]

def test_chatbot_initialization_and_chat():
    loader = DummyLoader()
    llm_client = DummyLLM()
    chatbot = BankingChatbotService(document_loader=loader, llm_client=llm_client)

    chatbot.initialize()

    response = chatbot.chat("Tell me about banking.")
    assert "Dummy" in response
    assert len(chatbot.chat_history) == 2  # User + Bot messages

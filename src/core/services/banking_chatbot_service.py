from llama_index.core import VectorStoreIndex, Settings
from src.core.interfaces.chatbot_service import ChatbotService
from src.core.interfaces.document_loader import DocumentLoader
from src.core.interfaces.llm_client import LLMClient

class BankingChatbotService(ChatbotService):
    def __init__(self, document_loader: DocumentLoader, llm_client: LLMClient):
        self.document_loader = document_loader
        self.llm_client = llm_client
        self.documents = None
        self.index = None
        self.query_engine = None
        self.chat_history = []

    def initialize(self) -> None:
        Settings.llm = self.llm_client.llm
        Settings.embed_model = self.llm_client.embedding
        self.documents = self.document_loader.load_documents()
        self.index = VectorStoreIndex.from_documents(self.documents)
        self.query_engine = self.index.as_query_engine(
            similarity_top_k=3,
            response_mode="tree_summarize",
            streaming=False
        )

    def chat(self, message: str) -> str:
        try:
            response = self.query_engine.query(message)
            response_text = response.response
            if response_text == "Empty Response" or not response_text.strip():
                fallback_context = self.documents[0].text[:1000]
                prompt = f"Based on this banking information: '{fallback_context}', please answer: {message}"
                response_text = self.llm_client.query(prompt)

            self.chat_history.append(("User", message))
            self.chat_history.append(("Bot", response_text))
            return response_text

        except Exception:
            return "Sorry, I cannot retrieve any data at this time. Please try again later."

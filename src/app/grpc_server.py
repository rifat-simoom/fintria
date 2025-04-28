import grpc
from concurrent import futures
import chat_pb2
import chat_pb2_grpc
from src.core.services.simple_directory_loader import SimpleDirectoryLoader
from src.core.services.ollama_llm_client import OllamaLLMClient
from src.core.services.banking_chatbot_service import BankingChatbotService

class BankingChatbotServicer(chat_pb2_grpc.BankingChatbotServicer):
    def __init__(self):
        doc_loader = SimpleDirectoryLoader(directory_path="docs")
        llm_client = OllamaLLMClient(model_name="mistral")
        self.chatbot_service = BankingChatbotService(document_loader=doc_loader, llm_client=llm_client)
        self.chatbot_service.initialize()

    def Chat(self, request, context):
        bot_reply = self.chatbot_service.chat(request.user_message)
        return chat_pb2.ChatResponse(bot_response=bot_reply)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_BankingChatbotServicer_to_server(BankingChatbotServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

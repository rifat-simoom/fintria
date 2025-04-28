
import grpc
import chat_pb2, chat_pb2_grpc
def test_grpc_chat():

    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = chat_pb2_grpc.BankingChatbotStub(channel)

        request = chat_pb2.ChatRequest(user_message="Tell me about loans")
        response = stub.Chat(request)

        assert hasattr(response, "bot_response"), "Missing 'bot_response' field"
        assert len(response.bot_response) > 0, "Empty bot response"

        print("[✅] gRPC API Test Passed!")
    except Exception as e:
        print(f"[❌] gRPC API Test Failed: {e}")


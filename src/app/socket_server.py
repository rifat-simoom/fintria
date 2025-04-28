import uvicorn
from fastapi import FastAPI, WebSocket
from src.core.services.simple_directory_loader import SimpleDirectoryLoader
from src.core.services.ollama_llm_client import OllamaLLMClient
from src.core.services.banking_chatbot_service import BankingChatbotService

app = FastAPI()

# Initialize chatbot service
doc_loader = SimpleDirectoryLoader(directory_path="docs")
llm_client = OllamaLLMClient(model_name="mistral")
chatbot_service = BankingChatbotService(document_loader=doc_loader, llm_client=llm_client)
chatbot_service.initialize()

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            user_message = await websocket.receive_text()
            bot_reply = chatbot_service.chat(user_message)
            await websocket.send_text(bot_reply)
        except Exception as e:
            await websocket.close()
            break


def main():
    # This runs the FastAPI app using uvicorn directly inside the script
    uvicorn.run(app, host="0.0.0.0", port=8001)

if __name__ == "__main__":
    main()
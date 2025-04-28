import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from src.core.services.simple_directory_loader import SimpleDirectoryLoader
from src.core.services.ollama_llm_client import OllamaLLMClient
from src.core.services.banking_chatbot_service import BankingChatbotService

app = FastAPI()

class ChatRequest(BaseModel):
    user_message: str

class ChatResponse(BaseModel):
    bot_response: str

# Initialize chatbot service
doc_loader = SimpleDirectoryLoader(directory_path="docs")
llm_client = OllamaLLMClient(model_name="mistral")
chatbot_service = BankingChatbotService(document_loader=doc_loader, llm_client=llm_client)
chatbot_service.initialize()

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    bot_reply = chatbot_service.chat(request.user_message)
    return ChatResponse(bot_response=bot_reply)
def main():
    # This runs the FastAPI app using uvicorn directly inside the script
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
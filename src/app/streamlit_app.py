import streamlit as st
from src.core.services.simple_directory_loader import SimpleDirectoryLoader
from src.core.services.ollama_llm_client import OllamaLLMClient
from src.core.services.banking_chatbot_service import BankingChatbotService

# Streamlit view (pure presentation layer)

st.title("🏦 Fintria AI")

if "chatbot_service" not in st.session_state:
    try:
        doc_loader = SimpleDirectoryLoader(directory_path="docs")
        llm_client = OllamaLLMClient(model_name="mistral")
        chatbot_service = BankingChatbotService(document_loader=doc_loader, llm_client=llm_client)

        st.write("Initializing system...")
        chatbot_service.initialize()

        st.session_state.chatbot_service = chatbot_service
        st.success("System initialized and ready!")
    except Exception as e:
        st.error(f"Initialization error: {str(e)}")
        st.stop()

user_input = st.text_input("Ask a banking question:")

if user_input:
    with st.spinner("Generating response..."):
        response = st.session_state.chatbot_service.chat(user_input)

    # Display chat history
    for role, message in st.session_state.chatbot_service.chat_history:
        if role == "User":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Bot:** {message}")

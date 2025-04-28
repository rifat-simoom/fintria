from src.core.services.ollama_llm_client import OllamaLLMClient


class FakeLLM:
    def complete(self, prompt):
        class Response:
            text = "This is a fake LLM response."

        return Response()


def test_llm_query(monkeypatch):
    client = OllamaLLMClient(model_name="mistral")

    # Instead of patching `complete`, patch the entire `.llm`
    monkeypatch.setattr(client, "llm", FakeLLM())

    result = client.query("Hello?")
    assert result == "This is a fake LLM response."

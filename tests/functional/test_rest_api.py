import requests


def test_rest_chat():
    url = "http://localhost:8000/chat"
    payload = {"user_message": "What is a checking account?"}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # raises HTTPError if not 200

        json_data = response.json()
        assert "bot_response" in json_data, "Missing 'bot_response' in response"
        assert len(json_data["bot_response"]) > 0, "Empty bot response"

        print("[✅] REST API Test Passed!")
    except Exception as e:
        print(f"[❌] REST API Test Failed: {e}")


if __name__ == "__main__":
    test_rest_chat()

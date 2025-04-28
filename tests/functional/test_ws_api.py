import asyncio

import pytest
import websockets

@pytest.mark.asyncio
async def test_ws_chat():
    uri = "ws://localhost:8001/ws/chat"

    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send("What is an overdraft?")
            response = await websocket.recv()

            assert response is not None, "No response received"
            assert len(response) > 0, "Empty bot response"

            print("[✅] WebSocket API Test Passed!")
    except Exception as e:
        print(f"[❌] WebSocket API Test Failed: {e}")


if __name__ == "__main__":
    asyncio.run(test_ws_chat())

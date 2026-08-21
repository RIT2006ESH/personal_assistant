# app/ollama_client.py

class OllamaClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def generate_answer(self, query: str) -> str:
        # Placeholder implementation
        return f"Answer to {query}"

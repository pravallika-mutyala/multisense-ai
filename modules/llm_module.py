import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_final_response(fusion_prompt):
    """
    Generate final response using DeepSeek via OpenRouter API.
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-r1",
        "messages": [
            {"role": "system", "content": "You are a helpful multimodal AI assistant."},
            {"role": "user", "content": fusion_prompt}
        ],
        "max_tokens": 200
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()

    if "error" in data:
        return "❌ Error: " + data["error"]["message"]

    return data["choices"][0]["message"]["content"]

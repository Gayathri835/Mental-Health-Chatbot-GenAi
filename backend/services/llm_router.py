import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_openrouter(prompt: str):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    res = requests.post(url, headers=headers, json=data)
    return res.json()["choices"][0]["message"]["content"]


def call_ollama(prompt: str):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "medgemma",
        "prompt": prompt
    }

    res = requests.post(url, json=data)
    return res.json().get("response", "")

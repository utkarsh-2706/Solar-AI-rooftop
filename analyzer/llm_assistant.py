from dotenv import load_dotenv
import os
import requests

load_dotenv()  # Load from .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def query_groq(prompt: str, model="llama3-70b-8192"):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful solar energy assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    url = "https://api.groq.com/openai/v1/chat/completions"
    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"

    return response.json()['choices'][0]['message']['content']

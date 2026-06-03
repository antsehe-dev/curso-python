from random import choices

import requests

# Peticiones API de groq
GROQ_API = "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"

def call_groq_api(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API}"
    }
    data ={
        "model": "llama-3.3-70b-versatile",
        "messages": [{
            "role": "user",
            "content": prompt
            }]
        }
    response = requests.post(url=url, json=data, headers=headers)
    print(response.json()["choices"][0]["message"]["content"])   

call_groq_api(input("Escribe tu pregunta para la API de Groq: "))



import streamlit as st
import requests

def call_api():
    url = "https://api.afforai.com/api/api_completion"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "apiKey": "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e",
        "sessionID": "65489d7c9ad727940f2ab26f",
        "history": [
            {
                "role": "user",
                "content": "What is AI?"
            }
        ],
        "powerful": False,
        "google": True
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

response = call_api()
st.write(response)

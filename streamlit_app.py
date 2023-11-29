import requests
import json
import streamlit as st
from streamlit.report_thread import get_report_ctx

# Session State Initialization
ctx = get_report_ctx()
if not hasattr(ctx, "session_state"):
    ctx.session_state = {"messages": [{"role": "assistant", "content": "¿En qué puedo ayudarte?"}]}

# Constants
AFFORAI_API_URL = "https://api.afforai.com/api/api_completion"
SESSION_ID = "65489d7c9ad727940f2ab26f"
AFFORAI_API_KEY = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"

# Chat Messages Display
for msg in ctx.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input and API Request
if prompt := st.chat_input():
    history = [{"role": "user", "content": prompt}]
    payload = {
        "sessionID": SESSION_ID,
        "history": history,
        "powerful": False,
        "google": True
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AFFORAI_API_KEY}"
    }

    try:
        response = requests.post(AFFORAI_API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        msg = response.json()
        ctx.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])
    except requests.exceptions.RequestException as e:
        st.error(f"Error en la solicitud de la API de Afforai: {e}")

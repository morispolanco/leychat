import requests
import json
import streamlit as st

st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "¿En qué puedo ayudarte?"}] 

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    session_id = "65489d7c9ad727940f2ab26f"
    history = [{"role": "user", "content": prompt}]
    payload = {
        "sessionID": session_id,
        "history": history,
        "powerful": False,
        "google": True
    }

    afforai_api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {afforai_api_key}"
    }

    response = requests.post("https://api.afforai.com/api/api_completion", headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        msg = response.json()
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])
    else:
        st.error("Error en la solicitud de la API de Afforai.")

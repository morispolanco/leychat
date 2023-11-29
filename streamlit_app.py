import streamlit as st
import requests

def call_api(message):
    url = "https://api.afforai.com/api/api_completion"
    payload = {
        "apiKey": "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e",
        "sessionID": "65489d7c9ad727940f2ab26f",
        "history": [
            {"role": "user", "content": message}
        ],
        "powerful": False,
        "google": True
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.title("Chatbot con Streamlit")
    
    message = st.text_input("Ingresa tu mensaje")
    
    if st.button("Enviar"):
        if message:
            response = call_api(message)
            
            if response:
                st.text(response)
            else:
                st.text("Error al llamar a la API")
        else:
            st.text("Por favor, ingresa un mensaje")

if __name__ == "__main__":
    main()

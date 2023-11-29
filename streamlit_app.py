import streamlit as st
import requests 

def call_api(message):
    url = "https://api.afforai.com/api/api_completion"
    payload = {
        "apiKey": "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e",
        "sessionID": "65489d7c9ad727940f2ab26f",
        "history": [{"role": "user", "content": message}],
        "powerful": False,
        "google": True
    }
    response = requests.post(url, json=payload)
    return response.json()

def main():
    st.title("Chatbot de IA")
    
    user_input = st.text_input("Usuario:", value="What is AI?")
    if st.button("Enviar"):
        response = call_api(user_input)
        st.markdown(f"**Bot:** {response['suggestedUserResponses'][0]}")

if __name__ == "__main__":
    main()

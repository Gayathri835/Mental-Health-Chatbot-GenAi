import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

st.title("Mental Health Chatbot")

user_input = st.text_input("How are you feeling today?")

if st.button("Send"):
    response = requests.post(API_URL, json={"message": user_input})
    data = response.json()

    st.write("Bot:", data["response"])

    if data.get("escalation"):
        st.warning("⚠️ Crisis detected. Seeking help...")

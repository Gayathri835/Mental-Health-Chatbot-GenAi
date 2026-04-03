import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

st.title("Mental Health Chatbot (GenAI)")

user_input = st.text_input("How are you feeling?")

if st.button("Send"):
    res = requests.post(API_URL, json={"message": user_input})
    data = res.json()

    st.write("Bot:", data["response"])

    if data["escalation"]:
        st.error("🚨 Emergency detected. Help is being contacted.")

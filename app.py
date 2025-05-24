import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("APKKEY")

client = OpenAI(api_key=api_key)

st.title("Fantasy Cricket Assistant Chatbot")

user_input = st.text_input("Ask me about Fantasy Cricket:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}],
        max_tokens=150,
    )
    st.write("Assistant:", response.choices[0].message.content)

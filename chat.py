import streamlit as st
import google.generativeai as genai
GEMINI_API_KEY = 'AIzaSyAn9ClF9wHaMYKhtr2T8yK_SUFKEJJJyXw'

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-3-flash-preview")

st.title("Gemini AI Chatbot")

user_input = st.text_input("Ask something")

if st.button("Send"):
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
import os
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))




# Set your OpenAI API key

st.title("LLM Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def generate_response(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ])
    return response.choices[0].message.content.strip()

def main():
    st.header("Chat with the bot")
    user_input = st.text_input("You:", key="input")

    if st.button("Send"):
        if user_input:
            st.session_state['messages'].append({"role": "user", "content": user_input})
            response = generate_response(user_input)
            st.session_state['messages'].append({"role": "bot", "content": response})

    for message in st.session_state['messages']:
        if message['role'] == 'user':
            st.text_area("You:", value=message['content'], key=f"user_{message['content']}", height=70)
        else:
            st.text_area("Bot:", value=message['content'], key=f"bot_{message['content']}", height=70)

if __name__ == "__main__":
    main()
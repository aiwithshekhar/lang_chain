import streamlit as st
import time
from langchain.llms import OpenAI
from openai.error import RateLimitError

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

def handle_rate_limit_error(error, input_text):
    st.error('Rate limit exceeded. Retrying in 30 seconds...')
    time.sleep(30)
    generate_response(input_text)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        try:
            generate_response(text)
        except RateLimitError as error:
            handle_rate_limit_error(error, text)

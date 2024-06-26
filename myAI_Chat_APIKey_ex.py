import streamlit as st
from langchain_community.llms import OpenAI

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

# Streamlit secrets에서 OpenAI API 키 가져오기
openai_api_key = st.secrets["openai"]["api_key"]

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)
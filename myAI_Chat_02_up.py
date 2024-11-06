# 설치 필요
# pip install langchain
import streamlit as st
from langchain_community.llms import OpenAI

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    prompt = """
    system: 너는 여행 서비스 챗봇이란다. 여행 관련된 정보만 제공할 수 있어. 사용자 입력에 친절하게 응답을 부탁해.
    사용자 입력 :
    """
    all_prompt = prompt + text
    generate_response(all_prompt)
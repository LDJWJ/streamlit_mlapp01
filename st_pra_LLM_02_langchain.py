# pip instal openai langchain_community streamlit
import streamlit as st
import google.generativeai as genai
from langchain_community.llms import OpenAI

# Streamlit 페이지 설정
st.set_page_config(page_title="ChatGPT AI 챗봇", page_icon=":robot:")

# Streamlit 앱 제목
st.title("🍎🍐 ChatGPT AI 챗봇 🥝🍆")

# API 키 입력 섹션
# api_key = st.text_input("Google API 키를 입력하세요:", type="password")

openai_api_key = st.sidebar.text_input('OpenAI API Key', type="password")

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))


# 기본 Streamlit UI
image_url = "https://github.com/LDJWJ/portfolio_template/blob/main/dalle_chatBot.png?raw=true"
st.image(image_url, width=512)  # 이미지 크기를 절반으로 설정
st.markdown('<h1>무엇이든 가능한 AI 챗봇 🧑</h1>', unsafe_allow_html=True)

with st.form('my_form'):
  text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    prompt = """
      너는 영리하고 똑똑한 챗봇이란다. 사용자 입력에 친절하게 응답을 부탁해. 모르는 내용은 모른다고 야이기를 하렴.
    """
    all_prompt = prompt + text
    generate_response(all_prompt)
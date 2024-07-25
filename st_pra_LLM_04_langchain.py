# pip instal openai langchain_community streamlit
import streamlit as st
import google.generativeai as genai
from langchain_community.llms import OpenAI
from langchain.chains  import ConversationChain
from langchain.memory  import ConversationBufferMemory


# Streamlit 페이지 설정
st.set_page_config(page_title="ChatGPT AI 챗봇", page_icon=":robot:")

# Streamlit 앱 제목
st.title("🍎🍐 ChatGPT AI 챗봇 🥝🍆")

# API 키 입력 섹션
# api_key = st.text_input("Google API 키를 입력하세요:", type="password")

openai_api_key = st.sidebar.text_input('OpenAI API Key', type="password")

# 메모리 초기화
memory = ConversationBufferMemory()

# OpenAI 모델 및 대화 체인 초기화 함수
# init_conversation 함수는 OpenAI API 키를 사용하여 OpenAI 모델과 대화 체인을 초기화
def init_conversation(api_key):
    llm = OpenAI(api_key=api_key)
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    return conversation

# generate_response 함수는 사용자의 입력을 받아 대화 체인을 통해 응답을 생성
def generate_response(input_text, conversation):
  response = conversation.predict(input=input_text)
  return response


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
      # 대화 체인 초기화
      conversation = init_conversation(openai_api_key)

      # 프롬프트 구성
      prompt = f"""
      너는 영리하고 똑똑한 챗봇이란다. 사용자 입력에 친절하게 응답을 부탁해. 모르는 내용은 모른다고 야이기를 하렴.
      사용자 입력 : {text}
      """
      # 응답 생성
      response = generate_response(prompt, conversation)
      st.info(response)

      # 메모리에 대화 저장
      memory.save_context({"input": text}, {"output": response})

      # 메모리에서 대화 불러오기
      history = memory.load_memory_variables({})
      st.write("대화 히스토리:")
      st.write(history["history"])
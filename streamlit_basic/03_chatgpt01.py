# openai, OpenAI: OpenAI API 호출을 위한 라이브러리
# streamlit: 웹 UI 프레임워크
# os: (현재 예제에서는 사용되지 않음) 환경 변수 접근 또는 파일 경로 처리 용도

import openai
import streamlit as st
from openai import OpenAI
import os

# Streamlit app
st.title("ChatGPT와 대화하기")

# 오른쪽 사이드바에 OpenAI API 키 입력란 추가
st.sidebar.title("설정")
openai_api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")

if not openai_api_key:
    st.sidebar.warning("OpenAI API 키를 입력하세요.")
    st.stop()

# client = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
client = OpenAI(api_key  = openai_api_key)

# 초기 대화 상태 설정
# Streamlit 앱은 새로고침마다 상태가 초기화되는데, st.session_state를 쓰면 
#   사용자별 세션에 데이터를 유지할 수 있음.
# st.session_state에는 여러 개의 변수를 자유롭게 지정하고 저장할 수 있음.
# 숫자, 문자열, 리스트(대화 이력 등) 저장 가능.
if "messages" not in st.session_state:
    st.session_state.messages = []

# 사용자 입력
user_input = st.text_input("당신:", key="user_input")

if st.button("전송") and user_input:
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", 
                                      "content": user_input})

    # OpenAI API 호출
    response = client.chat.completions.create (
        model = "gpt-4o-mini",
        messages = st.session_state.messages
    )

    # OpenAI 응답 추가
    response_message = response.choices[0].message.content
    # st.session_state.messages.append(response_message)
    st.session_state.messages.append({"role": "assistant", 
                                      "content": response_message})

    # 사용자 입력 초기화
    user_input = ""

# 대화 내용 표시
for message in st.session_state.messages:
    icon = "👤"  if message["role"] == "user" else "🤖"
    st.markdown(f"{icon}: {message['content']}")


import openai
import streamlit as st
from openai import OpenAI
import os

# Streamlit app
st.title("여행용 챗봇과 대화하기")

# 사이드바: API 키 입력
st.sidebar.title("설정")
openai_api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")
if not openai_api_key:
    st.sidebar.warning("OpenAI API 키를 입력하세요.")
    st.stop()

client = OpenAI(api_key=openai_api_key)

# 사이드바: 언어 선택
st.sidebar.subheader("언어 선택")
languages = {
    "한국어": "ko",
    "영어": "en",
    "일본어": "ja",
    "중국어": "zh"
}
selected_languages = st.sidebar.multiselect(
    "지원할 언어를 선택하세요:",
    list(languages.keys()),
    default=["한국어"]
)

# 시스템 프롬프트 생성 (선택 언어 반영)
system_prompt = (
    "당신은 여행에 관한 질문에 답하는 챗봇입니다. "
    "여행지 추천, 준비물, 문화, 음식 등 다양한 주제에 대해 친절하게 안내해 주세요. "
    f"답변은 다음 언어로 동시에 제공해 주세요: {', '.join(selected_languages)}."
)

# 초기 세션 상태 설정 (시스템 메시지 포함)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# 대화 초기화 버튼 (시스템 메시지 유지)
if st.button("대화 초기화"):
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# 사용자 입력창
user_input = st.text_input("사용자 : ", key="user_input")

# 전송 버튼
if st.button("전송") and user_input:
    # 1) 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 2) OpenAI API 호출
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )
    assistant_reply = response.choices[0].message.content

    # 3) 어시스턴트 메시지 추가
    st.session_state.messages.append({"role": "assistant", 
                                      "content": assistant_reply})

# 대화 내용 및 다국어 번역 출력
for message in st.session_state.messages:
    # 시스템 메시지는 출력하지 않음
    if message["role"] == "system":
        continue
    # 역할별 아이콘 선택
    if message["role"] == "user":
        icon = "👤"
    elif message["role"] == "assistant":
        icon = "🤖"
    else:
        icon = ""

    # 메시지 출력
    st.markdown(f"{icon} {message['content']}")

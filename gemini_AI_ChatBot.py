import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, AIMessage
import google.generativeai as genai
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Streamlit 페이지 설정
st.set_page_config(page_title="Gemini AI 챗봇", page_icon=":robot:")

# Google API 키 설정
GOOGLE_API_KEY = "여기에_당신의_API_키를_입력하세요"
genai.configure(api_key=GOOGLE_API_KEY)

# Gemini 모델 초기화
model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

# 대화 기록을 저장할 메모리 초기화
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=model, memory=memory, verbose=True)

# Streamlit 앱 제목
st.title("Gemini AI 챗봇")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 메시지 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 받기
if prompt := st.chat_input("무엇이 궁금하신가요?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # AI 응답 생성
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = conversation.predict(input=prompt)
        message_placeholder.markdown(response)
    
    # AI 응답을 세션 상태에 추가
    st.session_state.messages.append({"role": "assistant", "content": response})

# 대화 기록 지우기 버튼
if st.button("대화 기록 지우기"):
    st.session_state.messages = []
    memory.clear()
    st.experimental_rerun()
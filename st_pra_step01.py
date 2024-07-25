# 기본적인 텍스트 출력과 사용자 입력
import streamlit as st

st.title("나의 첫 Streamlit 앱")
st.write("안녕하세요! 이것은 기본적인 Streamlit 앱입니다.")

name = st.text_input("당신의 이름을 입력하세요")
if name:
    st.write(f"반갑습니다, {name}님!")
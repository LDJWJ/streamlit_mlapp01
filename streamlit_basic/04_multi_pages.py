
# Streamlit이 pages 디렉터리에 있는 파일을 페이지로 
# 자동 인식하도록 합니다. 이렇게 하면 사용자는 사이드바를 통해 
# 각 페이지로 이동할 수 있습니다. 
# 각 페이지는 독립적인 Streamlit 애플리케이션처럼 작동하므로 코드와 내용이 
# 독립적입니다.

import streamlit as st

st.title("Main Page")
st.write("Welcome to the main page!")

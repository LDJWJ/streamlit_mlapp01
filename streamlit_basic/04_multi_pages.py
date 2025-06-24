
# Streamlit이 pages 디렉터리에 있는 파일을 페이지로 
# 자동 인식하도록 합니다. 이렇게 하면 사용자는 사이드바를 통해 
# 각 페이지로 이동할 수 있습니다. 
# 각 페이지는 독립적인 Streamlit 애플리케이션처럼 작동하므로 코드와 내용이 
# 독립적입니다.

'''
your_app/
│
├── streamlit_app.py      ← 메인 페이지 스크립트
│
└── pages/                ← 추가 페이지들은 이 폴더에 넣기
    ├── 1_About.py        ← 페이지 파일명 앞에 숫자 붙이면 순서 지정 가능
    ├── 2_Contact.py
    └── 3_Help.py
'''



import streamlit as st

st.title("Main Page")
st.write("Welcome to the main page!")

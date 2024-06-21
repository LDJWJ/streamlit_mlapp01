import streamlit as st

# 사이드바 설정
st.sidebar.title("질문 목록")
st.sidebar.button("암")
st.sidebar.button("진단검사")
st.sidebar.button("치료도구")

st.sidebar.markdown("---")
st.sidebar.text("이용약관 | 개인정보처리방침")
st.sidebar.text("AI-Patent Korea")
st.sidebar.text("서울시 유성구 은구비로")

# 메인 화면 설정
st.title("스마트한 AI 특허비서")

st.write("### 특허 출원")
st.write("특허 출원 과정에서 필요한 모든 정보를 제공합니다. 어떤 절차를 밟아야 하는지, 필요한 서류는 무엇인지, AI 비서가 자세히 안내해드립니다.")

st.write("### 특허 검색")
st.write("특허 검색이 필요하신가요? AI 특허 비서가 여러분의 아이디어와 관련된 기존 특허를 신속하게 찾아드립니다.")

st.write("### 특허 전략")
st.write("특허 전략 수립에 도움이 필요하신가요? AI 특허 비서가 경쟁사 분석부터 포트폴리오 관리까지, 전략적인 조언을 제공합니다.")

st.write("### 특허 분쟁")
st.write("특허 분쟁이 발생했나요? AI 특허 비서가 법적 대응 방법과 전략을 제시해 드립니다.")

# 질문 입력란 및 버튼
st.text_input("질문하실 내용을 입력해주세요.", max_chars=100)
st.button("제출")

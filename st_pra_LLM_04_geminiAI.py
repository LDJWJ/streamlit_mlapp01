import streamlit as st
import google.generativeai as genai

# Streamlit 페이지 설정
st.set_page_config(page_title="Gemini AI 챗봇", page_icon=":robot:")

# Streamlit 앱 제목
st.title("Gemini AI 챗봇")

# API 키 입력 섹션
api_key = st.text_input("Google API 키를 입력하세요:", type="password")

# API 키가 입력되었을 때만 챗봇 기능 활성화
if api_key:
    try:
        # Google API 키 설정
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # 기본 Streamlit UI
        image_url = "https://github.com/LDJWJ/portfolio_template/blob/main/dalle_chatBot.png?raw=true"
        st.image(image_url, width=300)  # 이미지 크기를 절반으로 설정
        st.markdown('<h1>친절하고 똑똑한 AI 챗봇 🧑</h1>', unsafe_allow_html=True)

        # 세션 상태 초기화
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # 사용자 입력 받기
        user_input = st.text_input("원하는 것을 이야기해 주세요.")
        user_input_query = "\"" + user_input + "\"" + " 3-5줄 형태로 답변을 부탁해. 하지만 모르는 것은 만들어내지 말고 모른다고 답변을 부탁해."

        # '전송' 버튼 클릭 시 동작
        if st.button("📩"):  # 메시지 전송 아이콘 버튼
            # 모델에 사용자 입력 전달하여 응답 생성
            response = model.generate_content( user_input_query )

            # 생성된 응답 출력
            response_text = response.text

            st.write(response_text)

    except Exception as e:
        st.error(f"오류가 발생했습니다: {str(e)}")
else:
    st.warning("API 키를 입력해주세요.")

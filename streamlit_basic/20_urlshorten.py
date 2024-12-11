import streamlit as st
import pyshorteners

# Streamlit 앱
def main():
    st.title("URL 단축 서비스")

    st.write("""
    이 앱은 긴 URL을 짧은 URL로 변환하여 쉽게 공유할 수 있게 도와줍니다.
    긴 URL을 입력하면 단축된 URL을 얻을 수 있습니다.
    """)

    # 사용자로부터 긴 URL 입력 받기
    long_url = st.text_input("단축할 URL을 입력하세요:")

    if long_url:
        # URL 단축기 객체 생성
        s = pyshorteners.Shortener()

        try:
            # 긴 URL을 단축
            short_url = s.tinyurl.short(long_url)
            st.write(f"단축된 URL: {short_url}")
        except Exception as e:
            st.error(f"URL을 단축하는 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()

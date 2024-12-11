import streamlit as st
import qrcode
from PIL import Image
import io

# Streamlit 앱
def main():
    st.title("QR 코드 생성기")

    st.write("""
    이 앱은 텍스트나 URL을 QR 코드로 변환하여 이미지를 생성합니다.
    원하는 텍스트나 URL을 입력하면 QR 코드를 생성할 수 있습니다.
    """)

    # 사용자로부터 텍스트나 URL 입력 받기
    user_input = st.text_input("QR 코드를 생성할 텍스트 또는 URL을 입력하세요:")

    if user_input:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,  # QR 코드 버전 (1은 기본 21x21 크기)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 수정 수준
            box_size=10,  # 박스 크기
            border=4,  # 테두리 두께
        )
        qr.add_data(user_input)  # 입력된 데이터를 QR 코드에 추가
        qr.make(fit=True)

        # 이미지로 변환
        img = qr.make_image(fill='black', back_color='white')

        # PIL 이미지 객체를 바이트 스트림으로 변환
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        # 생성된 QR 코드 이미지 표시
        st.image(buf, caption="생성된 QR 코드", use_column_width=True)

if __name__ == "__main__":
    main()

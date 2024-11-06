# pip install streamlit qrcode pillow

import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# 앱 제목
st.title('QR Code Generator')

# 사용자가 입력할 텍스트 또는 URL
text = st.text_input("Enter text or URL to generate QR Code:")

# QR 코드 생성 버튼
if st.button('Generate QR Code'):
    if text:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,  # QR 코드 크기
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # 에러 보정 수준
            box_size=10,  # QR 코드 크기 조정
            border=4,  # 테두리 크기
        )
        qr.add_data(text)
        qr.make(fit=True)
        
        # QR 코드를 이미지로 변환
        img = qr.make_image(fill="black", back_color="white").convert('RGB')
        
        # 이미지를 스트림으로 변환하여 다운로드 가능하도록 설정
        buffered = BytesIO()
        img.save(buffered, format="PNG")  # 이미지 포맷을 PNG로 저장
        img_bytes = buffered.getvalue()

        # QR 코드 이미지 출력
        st.image(img, caption='Generated QR Code', use_column_width=True)

        # QR 코드 이미지 다운로드 링크 생성
        st.download_button(
            label="Download QR Code",
            data=img_bytes,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.error("Please enter some text or URL to generate the QR code.")


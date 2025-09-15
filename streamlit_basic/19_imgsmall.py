import streamlit as st
from PIL import Image
import io

# 이미지 크기 줄이는 함수
def resize_image(image, max_size):
    img = Image.open(image)
    img.thumbnail((max_size, max_size))
    return img

# Streamlit 앱
def main():
    st.title("이미지 크기 조정 앱")
    st.write("이미지를 업로드하고, 크기를 줄일 수 있습니다.")

    # 이미지 파일 업로드
    uploaded_file = st.file_uploader("이미지 파일을 업로드하세요", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # 이미지 보기
        st.image(uploaded_file, caption="업로드된 이미지", use_column_width=True)

        # 최대 크기 입력 받기
        max_size = st.slider("이미지의 최대 크기 (픽셀)", min_value=100, max_value=2000, value=800)

        # 이미지 크기 줄이기
        img = resize_image(uploaded_file, max_size)

        # 크기 줄인 이미지 보여주기
        st.image(img, caption="크기가 줄어든 이미지", use_column_width=True)

        # 이미지 다운로드 버튼
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        st.download_button(
            label="크기 줄인 이미지 다운로드",
            data=buffer,
            file_name="resized_image.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()

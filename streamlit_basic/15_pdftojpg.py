# pip install streamlit pdf2image pillow
# 01 poppler 프로그램 설치
#   - https://github.com/oschwartz10612/poppler-windows/releases/
#   - releases 파일 다운로드 후, 설치
# 
# 02 프로그램에 라이브러리 설치
#   - streamlit pdf2image pillow
# 
# 03 프로그램 실행 
 

import streamlit as st
from pdf2image import convert_from_bytes
from io import BytesIO
import zipfile

def convert_pdf_to_jpg(pdf_file):
    images = convert_from_bytes(pdf_file.read())
    return images

def main():
    st.title("PDF to JPG Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        if st.button("Convert to JPG"):
            images = convert_pdf_to_jpg(uploaded_file)
            
            # Create a ZIP file containing all converted images
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                for i, image in enumerate(images):
                    img_byte_arr = BytesIO()
                    image.save(img_byte_arr, format='JPEG')
                    zip_file.writestr(f"page_{i+1}.jpg", img_byte_arr.getvalue())
            
            # Offer the ZIP file for download
            st.download_button(
                label="Download JPG images",
                data=zip_buffer.getvalue(),
                file_name="converted_images.zip",
                mime="application/zip"
            )

if __name__ == "__main__":
    main()
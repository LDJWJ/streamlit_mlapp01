import streamlit as st

st.title("업무 도구 런처")
st.write("실행할 프로그램을 선택하세요.")

col1, col2 = st.columns(2)
with col1:
    if st.button("🗜️ PDF 압축기", use_container_width=True):
        st.switch_page("pages/1_About.py")
with col2:
    if st.button("🧩 PDF 합치기", use_container_width=True):
        st.switch_page("pages/2_Contact.py")

st.divider()
st.page_link("pages/1_About.py", label="PDF 압축기로 이동")
st.page_link("pages/2_Contact.py", label="PDF 합치기로 이동")

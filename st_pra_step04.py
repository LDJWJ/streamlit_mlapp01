# 데이터 캐싱, 인터랙티브 차트, 레이아웃 구성, 파일 업로드/다운로드
# 
import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.DataFrame({
        '날짜': pd.date_range(start='2023-01-01', periods=100),
        '판매량': [100 + i * 2 + (i % 7) * 10 for i in range(100)]
    })

st.title("인터랙티브 대시보드")

data = load_data()

st.write("데이터 미리보기:")
st.dataframe(data.head())

with st.expander("데이터 통계"):
    st.write(data.describe())

st.subheader("시계열 차트")
fig = px.line(data, x='날짜', y='판매량', title='일별 판매량')
st.plotly_chart(fig)

col1, col2 = st.columns(2)

with col1:
    st.subheader("파일 업로더")
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")
    if uploaded_file is not None:
        st.success("파일이 성공적으로 업로드되었습니다!")

with col2:
    st.subheader("다운로드 버튼")
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="CSV 다운로드",
        data=csv,
        file_name="sales_data.csv",
        mime="text/csv",
    )

if st.checkbox("원본 데이터 보기"):
    st.write(data)

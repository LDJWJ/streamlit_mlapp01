import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit 페이지 설정
st.set_page_config(page_title="데이터 시각화 앱", page_icon="📊")

st.title("차트와 사이드바를 활용한 데이터 시각화")

# 현재 실행 중인 앱의 URL 표시
st.write(f"이 앱은 다음 URL에서 실행 중입니다: {st.get_option('browser.serverAddress')}")

# 샘플 데이터 생성
data = pd.DataFrame({
    '월': ['1월', '2월', '3월', '4월', '5월'],
    '매출': [100, 150, 200, 180, 250]
})

st.sidebar.header("설정")
chart_type = st.sidebar.radio("차트 유형 선택", ["선 그래프", "막대 그래프"])

st.write("월별 매출 데이터:")
st.dataframe(data)

# Plotly를 사용한 차트 생성
if chart_type == "선 그래프":
    fig = px.line(data, x='월', y='매출', title="월별 매출")
else:
    fig = px.bar(data, x='월', y='매출', title="월별 매출")

fig.update_layout(
    xaxis_title="월",
    yaxis_title="매출",
    font=dict(family="Malgun Gothic, Arial", size=12)
)

st.plotly_chart(fig)

if st.button("데이터 분석"):
    st.write(f"총 매출: {data['매출'].sum():,}원")
    st.write(f"평균 매출: {data['매출'].mean():,.2f}원")

# 앱 정보 표시
st.info("이 앱은 Streamlit을 사용하여 만들어졌습니다.")
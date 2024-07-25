# 데이터프레임 표시와 간단한 필터링
import streamlit as st
import pandas as pd

st.title("간단한 데이터 분석기")

# 샘플 데이터 생성
data = pd.DataFrame({
    '이름': ['Alice', 'Bob', 'Charlie', 'David'],
    '나이': [25, 30, 35, 40],
    '도시': ['서울', '부산', '인천', '대전']
})

st.write("데이터 미리보기:")
st.dataframe(data)

selected_city = st.selectbox("도시를 선택하세요", data['도시'].unique())
filtered_data = data[data['도시'] == selected_city]

st.write(f"{selected_city}에 사는 사람들:")
st.table(filtered_data)
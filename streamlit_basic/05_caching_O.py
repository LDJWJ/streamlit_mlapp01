## 캐싱 있음.
# @st.cache_data: 이 데코레이터는 load_data 함수의 결과를 캐싱합니다. 
# 즉, 함수가 처음 실행될 때 데이터를 다운로드하고, 그 결과를 캐시
# 함수가 동일한 인수로 다시 호출될 때, 다운로드를 반복하지 않고 캐시된 결과를 반환
# 이렇게 하면 첫 번째 실행 이후에는 데이터가 즉시 로드되므로, 버튼을 클릭하여 
# 애플리케이션을 다시 실행해도 빠르게 데이터가 표시
import streamlit as st
import pandas as pd

@st.cache_data  # 데이터를 캐싱하는 데코레이터 추가
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")

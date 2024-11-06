## 캐싱 없이
# Uber 데이터셋을 다운로드하여 데이터프레임으로 로드
# 문제점: 다운로드는 인터넷 연결 속도에 따라 2초에서 30초까지 걸릴 수 있습니다. 버튼을 클릭하여 애플리케이션을 다시 실행할 때마다 
# 데이터를 다시 다운로드하기 때문에, 느린 사용자 경험을 제공
import streamlit as st
import pandas as pd

def load_data(url):
    df = pd.read_csv(url)  # 데이터를 다운로드하여 데이터프레임으로 로드
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")

## 캐싱 있음.
# @st.cache_data: 이 데코레이터는 load_data 함수의 결과를 캐싱합니다. 
# 즉, 함수가 처음 실행될 때 데이터를 다운로드하고, 그 결과를 캐시

'''
1. @st.cache_data 데코레이터
역할
 - 이 데코레이터를 붙인 함수(load_data)는 
 - 입력 인수가 동일할 때 이전 실행 결과를 저장(캐싱)해 둡니다.
 - 이후 같은 URL로 load_data를 호출하면, 
 - 인터넷에서 CSV를 다시 다운로드하지 않고 **캐시된 DataFrame**을 즉시 반환합니다.

효과
 -  첫 실행: load_data(url) → 실제로 pd.read_csv(url) 실행 → 결과 df 캐시에 저장
 -  두 번째 실행 이후(같은 url): 캐시에서 바로 df 꺼내 반환 → pd.read_csv 호출 비용 절감

사용 시 주의
 - 함수 인수가 바뀌면(다른 URL 등) 캐시가 무효화되고, 다시 다운로드

'''


import streamlit as st
import pandas as pd

@st.cache_data  # 데이터를 캐싱하는 데코레이터 추가
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")

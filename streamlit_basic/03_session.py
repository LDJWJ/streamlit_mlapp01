import streamlit as st
import pandas as pd
import numpy as np

# st.session_state: Streamlit의 세션 상태를 사용하여 
# 애플리케이션의 상태를 유지합니다. 
# 여기서는 데이터프레임 df가 세션 상태에 존재하지 않을 경우에만 생성
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), 
                                       columns=["x", "y"])
# st.header(...): 웹 페이지에 헤더를 추가
# st.color_picker(...): 사용자가 색상을 선택
# 구분선 추가: st.divider()
st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

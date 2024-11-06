# st.data_editor

import streamlit as st
import pandas as pd

# 샘플 데이터프레임 생성
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

# 편집 가능한 데이터프레임
edited_df = st.data_editor(df, num_rows="dynamic")  # 👈 동적 행 추가 및 삭제 활성화

# 사용자가 가장 선호하는 명령어 출력
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


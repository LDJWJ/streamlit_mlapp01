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
# num_rows="dynamic" 옵션으로 행 추가/삭제 기능을 활성화
edited_df = st.data_editor(df, num_rows="dynamic")  # 👈 동적 행 추가 및 삭제 활성화

# 사용자가 가장 선호하는 명령어 출력
# rating의 결과가 가장 높은 것.
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"당신의 가장 선호하는 명령은 **{favorite_command}** 🎈")


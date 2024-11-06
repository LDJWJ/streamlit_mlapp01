# Streamlit의 Session State를 사용하면 스크립트 재실행 시에도 
# 상태를 유지할 수 있습니다.
# 초기화, 읽기, 업데이트를 통해 Session State를 관리할 수 있습니다.
# Session State를 사용하면 더 나은 사용자 경험을 제공할 수 있습니다.

import streamlit as st

st.title('Counter Example')

# Session State 초기화
if 'count' not in st.session_state:
    st.session_state['count'] = 0

if 'cnt' not in st.session_state:
    st.session_state['cnt'] = 1

# Increment 버튼
increment = st.button('Increment')
if increment:
    st.session_state['count'] += 1
    st.session_state['cnt'] *= 2

# Count 출력
st.write('Count = ', st.session_state['count'])
st.write('cnt = ', st.session_state['cnt'])

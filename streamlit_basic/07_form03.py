# 이 패턴은 폼 제출 후 즉시 결과를 업데이트해야 할 때 사용합니다. 
# st.rerun은 폼 제출 후 스크립트를 다시 실행하여 최신 값을 반영
import streamlit as st

# 세션 상태에 'sum' 값이 없다면 초기화합니다.
if 'sum' not in st.session_state:
    st.session_state.sum = ''

# 두 개의 컬럼을 생성합니다.
col1, col2 = st.columns(2)
col1.title('Sum:')  # 첫 번째 컬럼에 제목을 설정합니다.

# 세션 상태의 'sum' 값이 float 타입이면 두 번째 컬럼에 출력합니다.
if isinstance(st.session_state.sum, float):
    col2.title(f'{st.session_state.sum:.2f}')

# 'addition'이라는 이름의 폼을 생성합니다.
with st.form('addition'):
    a = st.number_input('a')  # 첫 번째 숫자 입력 필드
    b = st.number_input('b')  # 두 번째 숫자 입력 필드
    submit = st.form_submit_button('add')  # 폼 제출 버튼

# 세션 상태의 'sum' 값을 입력된 'a'와 'b'의 합으로 업데이트합니다.
st.session_state.sum = a + b

# 폼이 제출되었을 때 스크립트를 다시 실행합니다.
if submit:
    st.rerun()

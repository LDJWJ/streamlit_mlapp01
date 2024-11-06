# 세션 상태와 콜백을 사용하여 폼 제출시 프로세스 실행
# 이 패턴은 폼 제출 시 실행할 복잡한 로직이 있을 때 유용합니다. 콜백 함수 내에서 세션 상태를 직접 업데이트하여 최신 값을 사용
import streamlit as st

# 세션 상태에 'sum' 값이 없다면 초기화합니다.
if 'sum' not in st.session_state:
    st.session_state.sum = ''

# 콜백 함수 정의
def sum():
    result = st.session_state.a + st.session_state.b  # 'a'와 'b'의 합을 계산
    st.session_state.sum = result  # 계산 결과를 세션 상태에 저장

# 두 개의 컬럼을 생성합니다.
col1, col2 = st.columns(2)
col1.title('Sum:')  # 첫 번째 컬럼에 제목을 설정합니다.

# 세션 상태의 'sum' 값이 float 타입이면 두 번째 컬럼에 출력합니다.
if isinstance(st.session_state.sum, float):
    col2.title(f'{st.session_state.sum:.2f}')

# 'addition'이라는 이름의 폼을 생성합니다.
with st.form('addition'):
    st.number_input('a', key='a')  # 첫 번째 숫자 입력 필드
    st.number_input('b', key='b')  # 두 번째 숫자 입력 필드
    st.form_submit_button('add', on_click=sum)  # 폼 제출 버튼과 콜백 함수 지정


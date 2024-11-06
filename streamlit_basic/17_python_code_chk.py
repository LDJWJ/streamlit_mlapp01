### 파이썬 샘플 코드 작성기

import streamlit as st
import sys
import io

# 앱 제목
st.title('Python Code Executor')

# 코드 입력받기
code_input = st.text_area("Enter your Python code below:", height=200)

# 코드 실행 버튼
if st.button('Run Code'):
    if code_input:
        # stdout, stderr를 캡처하기 위해 io.StringIO 사용
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()

        try:
            # 입력된 Python 코드를 실행
            exec(code_input)
            output = redirected_output.getvalue()
            st.success("Code executed successfully!")
            st.text_area("Output:", output, height=200)
        except Exception as e:
            error = redirected_error.getvalue() + str(e)
            st.error(f"An error occurred:\n{error}")

        # stdout, stderr를 원래 상태로 복원
        sys.stdout = old_stdout
        sys.stderr = old_stderr
    else:
        st.warning("Please enter some code to execute.")


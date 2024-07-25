# import google.generativeai as genai
# pip install -q -U google-generativeai
# 튜토리얼 : https://ai.google.dev/gemini-api/docs/get-started/tutorial?hl=ko&lang=python

# # 모델 설정
# model = genai.GenerativeModel('gemini-pro') # 텍스트 전용 모델

# # 답변 내용 보기
# print(response)
import pathlib
import textwrap
 
import google.generativeai as genai
 
from IPython.display import display
from IPython.display import Markdown
from config import Config
 
# 서식이 지정된 Markdown 텍스트를 표시하는 함수
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
 
# 제미나이 API 키 설정
genai.configure(api_key=Config.GOOGLE_API_KEY)
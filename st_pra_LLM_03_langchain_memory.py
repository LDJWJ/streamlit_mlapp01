# pip instal openai langchain_community streamlit
from langchain_community.llms import OpenAI
from langchain.chains  import ConversationChain
from langchain.memory  import ConversationBufferMemory
import getpass

# OpenAI API 키 설정 (password 형태로 입력받기)
api_key = getpass.getpass("Enter your OpenAI API key: ")
llm = OpenAI(api_key=api_key)

# 메모리 초기화
memory = ConversationBufferMemory()

# 대화 체인 초기화
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# 대화 예제
user_input1 = "안녕"
response1 = conversation.predict(input=user_input1)
print("AI:", response1)

user_input2 = "나의 이름은 토돌이야"
response2 = conversation.predict(input=user_input2)
print("AI:", response2)

user_input3 = "방금 말한 나의 이름이 뭐니?"
response3 = conversation.predict(input=user_input3)
print("AI:", response3)
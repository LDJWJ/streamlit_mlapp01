### Streamlit의 모든 SQL 연결은 SQLAlchemy를 사용
# pip install SQLAlchemy==1.4.0

# 단계 2: Streamlit secrets.toml 파일에 데이터베이스 URL 설정
# Streamlit 애플리케이션이 실행될 디렉토리에 .streamlit 디렉토리를 만들고, 
# 그 안에 secrets.toml 파일을 생성

import streamlit as st
import sqlalchemy as sa
import pandas as pd

# secrets.toml 에 정의된 URL 불러오기
# 이 방식으로 민감 정보(API 키나 DB 접속 정보)를 코드에 하드코딩하지 않고 안전하게 관리
conn_url = st.secrets["connections"]["pets_db"]["url"]

# 2) SQLAlchemy의 엔진(Engine) 객체를 생성
engine = sa.create_engine(conn_url)

# ▶ 변경: engine.begin() 사용하여 트랜잭션 블록을 만듦
# 3) 트랜잭션 블록: engine.begin()을 사용해 커밋을 자동 처리
# 이 블록 안에서 실행된 모든 DDL(테이블 생성)·DML(INSERT, DELETE) 문은 블록이 끝날 때 자동으로 COMMIT
# 별도 connection.commit() 호출이 필요 없음.
with engine.begin() as connection:

    # 3-1) 테이블 생성: 없으면 만들어라
    connection.execute(sa.text(
        "CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT)"
    ))

    # 3-2) 기존 데이터 삭제: 매번 “새로 초기화” 용도
    connection.execute(sa.text("DELETE FROM pet_owners"))

    # 3-3) 파이썬 dict에 담긴 데이터를 반복문으로 INSERT
    pet_owners = {"제리": "금붕어", "바바라": "고양이", "알렉스": "강아지"}
    for owner, pet in pet_owners.items():
        connection.execute(
            sa.text(
                "INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet)"
            ),
            {"owner": owner, "pet": pet}
        )

# 4) 조회 블록: engine.connect() + SELECT
with engine.connect() as connection:
    result = connection.execute(sa.text("SELECT * FROM pet_owners"))

    # fetchall()로 튜플 목록을 받고,
    # keys()로 컬럼명을 가져와 판다스 DataFrame으로 변환
    pet_owners_df = pd.DataFrame(result.fetchall(), columns=result.keys())

st.dataframe(pet_owners_df)


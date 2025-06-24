### Streamlit의 모든 SQL 연결은 SQLAlchemy를 사용
# pip install SQLAlchemy==1.4.0

# 단계 2: Streamlit secrets.toml 파일에 데이터베이스 URL 설정
# Streamlit 애플리케이션이 실행될 디렉토리에 .streamlit 디렉토리를 만들고, 
# 그 안에 secrets.toml 파일을 생성
'''
[connections]

[connections.iris_db]
url = "sqlite:///./iris.db"
'''



import streamlit as st
import sqlalchemy as sa
import pandas as pd
import seaborn as sns

# 1) seaborn에서 iris 데이터셋 로드 → pandas DataFrame으로 변환
df_iris = sns.load_dataset("iris")
# 컬럼: sepal_length, sepal_width, petal_length, petal_width, species

# 2) Streamlit secrets.toml 에 선언된 DB URL 불러오기
# 기존 pets_db → iris_db 로 변경
conn_url = st.secrets["connections"]["iris_db"]["url"]
engine = sa.create_engine(conn_url)

# 3) 트랜잭션 블록: 테이블 생성·삭제·삽입 후 자동 커밋
with engine.begin() as connection:
    # 3-1) iris 테이블 생성 (없으면)
    connection.execute(sa.text("""
        CREATE TABLE IF NOT EXISTS iris (
            sepal_length  REAL,
            sepal_width   REAL,
            petal_length  REAL,
            petal_width   REAL,
            species       TEXT
        )
    """))

    # 3-2) 기존 데이터 삭제
    connection.execute(sa.text("DELETE FROM iris"))

    # 3-3) DataFrame 행 단위로 INSERT
    for row in df_iris.itertuples(index=False):
        connection.execute(
            sa.text("""
                INSERT INTO iris
                    (sepal_length, sepal_width, petal_length, petal_width, species)
                VALUES
                    (:sl, :sw, :pl, :pw, :sp)
            """),
            {
                "sl": row.sepal_length,
                "sw": row.sepal_width,
                "pl": row.petal_length,
                "pw": row.petal_width,
                "sp": row.species
            }
        )

# 4) 조회 블록: SELECT 후 DataFrame으로 변환
with engine.connect() as connection:
    result = connection.execute(sa.text("SELECT * FROM iris"))
    iris_df = pd.DataFrame(result.fetchall(), columns=result.keys())

# 5) Streamlit에 표시
st.header("Iris 테이블 (seaborn → DB)")
st.dataframe(iris_df)


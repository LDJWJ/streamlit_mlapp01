### Streamlit의 모든 SQL 연결은 SQLAlchemy를 사용
# pip install SQLAlchemy==1.4.0

# 단계 2: Streamlit secrets.toml 파일에 데이터베이스 URL 설정
# Streamlit 애플리케이션이 실행될 디렉토리에 .streamlit 디렉토리를 만들고, 
# 그 안에 secrets.toml 파일을 생성
import streamlit as st
import sqlalchemy as sa
import pandas as pd
import seaborn as sns

# secrets 파일에 지정된 대로 pets_db에 대한 SQL 연결 생성
conn = st.secrets["connections"]["pets_db"]["url"]

# SQLAlchemy를 사용하여 엔진 생성
engine = sa.create_engine(conn)

# 연결을 사용하여 데이터 삽입
with engine.connect() as connection:
    connection.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    connection.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for owner, pet in pet_owners.items():
        connection.execute(
            sa.text('INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);'),
            {'owner': owner, 'pet': pet}
        )

# 삽입된 데이터를 쿼리하고 표시
with engine.connect() as connection:
    result = connection.execute('SELECT * FROM pet_owners')
    pet_owners = pd.DataFrame(result.fetchall(), columns=result.keys())

st.dataframe(pet_owners)

# seaborn을 사용하여 iris 데이터 불러오기
iris_df = sns.load_dataset('iris')

# iris 테이블 생성 및 데이터 삽입
with engine.connect() as connection:
    connection.execute('CREATE TABLE IF NOT EXISTS iris (sepal_length FLOAT, sepal_width FLOAT, petal_length FLOAT, petal_width FLOAT, species TEXT);')
    connection.execute('DELETE FROM iris;')
    iris_df.to_sql('iris', con=connection, if_exists='append', index=False)

# iris 데이터를 쿼리하고 표시
with engine.connect() as connection:
    result = connection.execute('SELECT * FROM iris')
    iris_db_df = pd.DataFrame(result.fetchall(), columns=result.keys())

st.dataframe(iris_db_df)

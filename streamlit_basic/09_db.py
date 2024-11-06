### Streamlit의 모든 SQL 연결은 SQLAlchemy를 사용
# pip install SQLAlchemy==1.4.0

# 단계 2: Streamlit secrets.toml 파일에 데이터베이스 URL 설정
# Streamlit 애플리케이션이 실행될 디렉토리에 .streamlit 디렉토리를 만들고, 
# 그 안에 secrets.toml 파일을 생성

import streamlit as st
import sqlalchemy as sa
import pandas as pd

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.secrets["connections"]["pets_db"]["url"]

# Use SQLAlchemy to create an engine
engine = sa.create_engine(conn)

# Insert some data with a connection
with engine.connect() as connection:
    connection.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    connection.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for owner, pet in pet_owners.items():
        connection.execute(
            sa.text('INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);'),
            {'owner': owner, 'pet': pet}
        )

# Query and display the data you inserted
with engine.connect() as connection:
    result = connection.execute('SELECT * FROM pet_owners')
    pet_owners = pd.DataFrame(result.fetchall(), columns=result.keys())

st.dataframe(pet_owners)


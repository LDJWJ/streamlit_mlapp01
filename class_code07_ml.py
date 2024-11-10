import streamlit as st  
import seaborn as sns  
from sklearn.linear_model import LinearRegression  

# 제목  
st.title('팁 예측 앱')  

# 데이터 로드  
tips = sns.load_dataset("tips")  

# 데이터 준비 및 모델 학습  
X = tips['total_bill'].values.reshape(-1, 1)  
y = tips['tip'].values  
model = LinearRegression()  
model.fit(X, y)  

# 입력값 받기  
total_bill = st.number_input('계산서 금액을 입력하세요:', min_value=0.0, value=50.0)  

# 예측하기  
if total_bill:  
    prediction = model.predict([[total_bill]])[0]  
    st.write(f'예상 팁 금액: ${prediction:.2f}')  

# 모델 정보 표시  
st.write('---')  
st.write('모델 정보:')  
st.write(f'- Intercept: {model.intercept_:.2f}')  
st.write(f'- Coefficient: {model.coef_[0]:.2f}')  

# 데이터 미리보기  
st.write('---')  
st.write('데이터 미리보기:')  
st.dataframe(tips.head()) 
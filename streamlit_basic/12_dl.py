#  전이학습을 위해 TensorFlow 또는 PyTorch와 같은 딥러닝 라이브러리를 사용할 수 있습니다. 
# 여기서는 TensorFlow와 Keras를 사용하여 전이학습 모델을 구축

# 코드 설명
# 코드 설명
# 라이브러리 임포트: Streamlit, TensorFlow, PIL, numpy 등의 라이브러리를 임포트합니다.
# 이미지 업로드 인터페이스: st.file_uploader를 사용하여 사용자가 이미지를 업로드할 수 있는 인터페이스를 만듭니다.
# 이미지 표시: 업로드된 이미지를 Streamlit을 통해 표시합니다.
# 이미지 전처리: 업로드된 이미지를 MobileNetV2 모델의 입력 크기인 224x224로 조정하고, 모델이 요구하는 형식으로 전처리합니다.
# 전이학습 모델 로드: MobileNetV2 모델을 ImageNet 가중치로 로드합니다.
# 예측 수행: 모델을 사용하여 이미지를 예측하고, 예측 결과를 디코딩하여 표시합니다.


import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from PIL import Image
import numpy as np

# Streamlit 애플리케이션 타이틀 설정
st.title("이미지 분류 애플리케이션")
st.write("전이학습을 사용하여 이미지를 분류합니다.")

# 이미지 업로드
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 이미지를 불러와서 표시
    img = Image.open(uploaded_file)
    st.image(img, caption="업로드한 이미지", use_column_width=True)

    # 이미지 전처리
    img = img.resize((224, 224))  # MobileNetV2 입력 크기로 조정
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # 전이학습 모델 로드 (MobileNetV2)
    model = MobileNetV2(weights="imagenet")

    # 예측 수행
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # 예측 결과 표시
    st.write("예측 결과:")
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        st.write(f"{i+1}. {label}: {score*100:.2f}%")


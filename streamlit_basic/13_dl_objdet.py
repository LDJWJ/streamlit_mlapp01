# 코드 설명
# 라이브러리 임포트: Streamlit, OpenCV, numpy, PIL 등을 임포트합니다.
# 클래스 이름 로드: coco.names 파일을 읽어 객체 클래스 이름을 리스트로 저장합니다.
# 네트워크 설정: yolov3.weights와 yolov3.cfg 파일을 사용하여 YOLOv3 모델을 로드하고, 출력 레이어를 설정합니다.
# 이미지 전처리 및 예측 함수: 이미지를 전처리하고, YOLO 모델을 사용하여 객체를 예측하는 predict 함수를 정의합니다.
# 객체 인식 결과 표시: 업로드된 이미지에 대해 예측을 수행하고, 예측된 객체를 이미지에 표시합니다.

import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Streamlit 애플리케이션 타이틀 설정
st.title("객체 인식 애플리케이션")
st.write("YOLOv3를 사용하여 이미지를 분석합니다.")

# 파일 업로드
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

# 클래스 이름 로드
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# 네트워크 설정
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def predict(image):
    height, width, channels = image.shape
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    return boxes, confidences, class_ids, indexes

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 이미지", use_column_width=True)
    
    image = np.array(image)
    boxes, confidences, class_ids, indexes = predict(image)
    
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, label, (x, y - 10), font, 1, color, 2)
    
    st.image(image, caption="객체 인식 결과", use_column_width=True)

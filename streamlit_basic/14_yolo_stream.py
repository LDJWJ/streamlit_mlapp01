import streamlit as st
import cv2
import numpy as np
import requests
from PIL import Image
import os

# YOLO 모델 파일 다운로드 함수
def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

# YOLO 모델 파일 다운로드
YOLO_WEIGHTS_URL = "https://pjreddie.com/media/files/yolov3.weights"
YOLO_CONFIG_URL = "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg"
YOLO_NAMES_CONTENT = """person
bicycle
car
motorbike
aeroplane
bus
train
truck
boat
traffic light
fire hydrant
stop sign
parking meter
bench
bird
cat
dog
horse
sheep
cow
elephant
bear
zebra
giraffe
backpack
umbrella
handbag
tie
suitcase
frisbee
skis
snowboard
sports ball
kite
baseball bat
baseball glove
skateboard
surfboard
tennis racket
bottle
wine glass
cup
fork
knife
spoon
bowl
banana
apple
sandwich
orange
broccoli
carrot
hot dog
pizza
donut
cake
chair
sofa
pottedplant
bed
diningtable
toilet
tvmonitor
laptop
mouse
remote
keyboard
cell phone
microwave
oven
toaster
sink
refrigerator
book
clock
vase
scissors
teddy bear
hair drier
toothbrush"""

# 파일 경로 설정
weights_path = "yolov3.weights"
config_path = "yolov3.cfg"
names_path = "coco.names"

# 파일 다운로드 및 저장
if not os.path.exists(weights_path):
    st.info("yolov3.weights 파일을 다운로드 중입니다...")
    download_file(YOLO_WEIGHTS_URL, weights_path)

if not os.path.exists(config_path):
    st.info("yolov3.cfg 파일을 다운로드 중입니다...")
    download_file(YOLO_CONFIG_URL, config_path)

if not os.path.exists(names_path):
    with open(names_path, 'w') as f:
        f.write(YOLO_NAMES_CONTENT)

# 클래스 이름 로드
with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# 네트워크 설정
net = cv2.dnn.readNet(weights_path, config_path)
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

def process_video(video_file):
    video = cv2.VideoCapture(video_file)
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        boxes, confidences, class_ids, indexes = predict(frame)

        font = cv2.FONT_HERSHEY_PLAIN
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y - 10), font, 1, color, 2)

        st.image(frame, channels="BGR")

# Streamlit 애플리케이션 타이틀 설정
st.title("실시간 영상 객체 인식 애플리케이션")
st.write("YOLOv3를 사용하여 실시간 영상에서 객체를 분석합니다.")

uploaded_file = st.file_uploader("동영상을 업로드하세요", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    st.write("업로드한 동영상:")
    process_video(uploaded_file)

import streamlit as st
import cv2

# Title and button to start camera
st.title("Motion Detector")
start = st.button("Start Camera")

# Action if the button has been clicked
if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(1)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text="Thoursday", org=(75, 75),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3,
                    color=(35, 50, 120), thickness=3, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

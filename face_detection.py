import cv2
import numpy as np
from fer import FER
def face_detection():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(0)
    
    if not video_capture.isOpened():
        print("Error accessing the camera")
        return

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error reading frame from webcam")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
def emotion_detection():
    emotion_detector = FER()
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error reading frame from webcam")
            break
        emotions = emotion_detector.detect_emotions(frame)
        if emotions:
            emotion_data = emotions[0]
            highest_confidence_emotion = max(emotion_data["emotions"], key=emotion_data["emotions"].get)
            (x, y, w, h) = emotion_data["box"]  
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) 
            cv2.putText(frame, highest_confidence_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        cv2.putText(frame,"Key Q to close",(20,30),cv2.FONT_HERSHEY_PLAIN,1,(200,100,200),1)
        cv2.imshow('Emotion Detector', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    emotion_detection()

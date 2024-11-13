import argparse
import cv2
import numpy as np
import math

def highlightFace(net, frame, conf_threshold=0.7):
    frameOpenCvDnn = frame.copy()
    frameHeight = frameOpenCvDnn.shape[0]
    frameWidth = frameOpenCvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpenCvDnn, 1.0, (300, 300), [103, 117, 123], True, False)
    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence >= conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpenCvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
    return frameOpenCvDnn, faceBoxes

parser = argparse.ArgumentParser()
parser.add_argument('--image')
args = parser.parse_args()

def age_gender_detection():
    video = cv2.VideoCapture(args.image if args.image else 0)
    padding = 20
    while cv2.waitKey(1) & 0xFF != ord('q'):
        hasFrame, frame = video.read()
        if not hasFrame:
            cv2.waitKey()
            break
        resultImg, faceBoxes = highlightFace(faceNet, frame)
        cv2.putText(resultImg,"Key Q to close",(20,30),cv2.FONT_HERSHEY_PLAIN,1,(200,100,200),1)
        for faceBox in faceBoxes:
            face = frame[max(0, faceBox[1]-padding):min(faceBox[3]+padding, frame.shape[0]-1),
                        max(0, faceBox[0]-padding):min(faceBox[2]+padding, frame.shape[1]-1)]
            
            if face.size == 0:
                continue
            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), model_Mean_value, False)
            gender=gender_detection(blob)
            age=age_detection(blob)
            cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1] - 10), 
                        cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
            
        cv2.imshow('Detection', resultImg)

def gender_detection(blob):
    genderNet.setInput(blob)
    genderPreds = genderNet.forward()
    gender = genderList[genderPreds[0].argmax()]
    return gender
def age_detection(blob):
    ageNet.setInput(blob)
    agePreds = ageNet.forward()
    age = ageList[agePreds[0].argmax()]
    return age

if __name__=="__main__":
    faceModel = 'opencv_face_detector_uint8.pb'
    faceProto = 'opencv_face_detector.pbtxt'
    ageModel = 'age_net.caffemodel'
    ageProto = 'age_deploy.prototxt'
    genderModel = 'gender_net.caffemodel'
    genderProto = 'gender_deploy.prototxt'
    model_Mean_value = (78.43, 87.76, 114.89)
    ageList = ['(0-3)', '(4-7)', '(8-12)', '(13-17)', '(18-25)', '(26-35)', '(36-45)', '(46-55)', '(56-65)', '(66-75)', '(76-85)', '(86+)']
    genderList = ['Male', 'Female']
    faceNet = cv2.dnn.readNet(faceModel, faceProto)
    ageNet = cv2.dnn.readNet(ageModel, ageProto)
    genderNet = cv2.dnn.readNet(genderModel, genderProto)
    age_gender_detection()

import cv2
import time
import os
import mediapipe as mp

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands()  #considering all default values
mpDraw = mp.solutions.drawing_utils

prevTime = 0
currTime = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLM in results.multi_hand_landmarks:

            for id, lm in enumerate(handLM.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(cx, cy)

                if (id == 0):
                    cv2.circle(img, (cx, cy), 15, (255, 0, 230), cv2.FILLED)
            mpDraw.draw_landmarks(
                img, handLM, mpHands.HAND_CONNECTIONS
            )  #HAND_CONNECTIONS used for drawing the lines between points

    currTime = time.time()
    fps = 1 / (currTime - prevTime)
    prevTime = currTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1,
                (234, 0, 200), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
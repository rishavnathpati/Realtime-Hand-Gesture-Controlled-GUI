import math
import os
import time
import numpy as np

import cv2
import HandTrackingModue as htm
from MultithreadedWebcam import VideoCaptureThreading
from pynput.mouse import Button, Controller

mouse = Controller()

cap = VideoCaptureThreading()
cap.start()

prevTime = 0
currTime = 0
sx, sy = 1920, 1080
camx, camy = 1280, 720
pinchFlag = 0

detector = htm.HandDetector()

mouseLocOld = np.array([0, 0])
mouseLoc = np.array([0, 0])
Dampingfactor = 2

# mouseLoc = mouseLocOld + (targetLoc - mouseLocOld) / Dampingfactor


def volumeControl(x1, y1, x2, y2):
    length = math.hypot(x2 - x1, y2 - y1)

    if (length < 50):
        cv2.circle(img, (cx12, cy12), 5, (5, 255, 2), cv2.FILLED)
        os.system('pactl set-sink-volume 0 0')
    else:
        vol = int(((int(length) - 50) / 250) * 150)
        command = 'pactl set-sink-volume 0 ' + str(vol) + '%'
        print(command)
        os.system(command)


def mouseControl(img, cx12, cy12, x1, y1, x2, y2):
    global pinchFlag, mouseLocOld, mouseLoc
    length = math.hypot(x2 - x1, y2 - y1)
    print(length)
    if (length < 30):
        if (pinchFlag == 0):
            pinchFlag = 1
            mouse.press(Button.left)
            cv2.circle(img, (cx12, cy12), 5, (255, 255, 255), cv2.FILLED)
        # mouseloc = (cx12 * sx / camx, cy12 * sy / camy)
        mouseLoc = mouseLocOld + ((x1, y1) - mouseLocOld) / Dampingfactor
        mouse.position = mouseLoc
        mouseLocOld = mouseLoc

    elif (length > 50):
        if (pinchFlag == 1):
            pinchFlag = 0
            mouse.release(Button.left)
        # mouseLoc = (cx12 * sx / camx, cy12 * sy / camy)
        mouseLoc = mouseLocOld + ((x1, y1) - mouseLocOld) / Dampingfactor
        mouse.position = mouseLoc
        mouseLocOld = mouseLoc

    return img


while (1):
    key = cv2.waitKey(1) & 0xFF
    success, img = cap.read()
    # img = cv2.flip(img, 1)

    img = detector.findhands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) != 0:
        # print(lmlist)

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        # x3, y3 = lmlist[12][1], lmlist[12][2]
        # x4, y4 = lmlist[16][1], lmlist[16][2]
        # x5, y5 = lmlist[20][1], lmlist[20][2]

        cx12, cy12 = int((x1 + x2) / 2), int((y1 + y2) / 2)

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx12, cy12), 5, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 1)

        if (key == ord('v')):
            volumeControl(x1, y1, x2, y2)
        img = mouseControl(img, cx12, cy12, x1, y1, x2, y2)

    currTime = time.time()
    fps = 1 / (currTime - prevTime)
    prevTime = currTime

    cv2.putText(img, str(int(fps)), (10, 20), cv2.FONT_HERSHEY_COMPLEX, 1,
                (255, 255, 255), 1)

    cv2.imshow("Image", img)
    if key == ord('q'):
        cap.stop()
        break
import cv2
import numpy as np
import time
from MultithreadedWebcam import VideoCaptureThreading
import HandTrackingModue as htm
import math
import os
from pynput.keyboard import Key, Controller

# wcam, hcam = 640, 480
# x1, y1, x2, y2, cx, cy = [0 for _ in range(6)]

cap = VideoCaptureThreading()
cap.start()
# cap.set(3, wcam)
# cap.set(4, hcam)

prevTime = 0
currTime = 0

detector = htm.HandDetector(detectionConfidence=0.8)

while (1):
    key = cv2.waitKey(1) & 0xFF
    success, img = cap.read()

    img = detector.findhands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) != 0:
        # print(lmlist)
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]

        cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 1)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)

        if (length < 50):
            cv2.circle(img, (cx, cy), 5, (5, 255, 2), cv2.FILLED)
            os.system('pactl set-sink-volume 0 0')
        else:
            vol = int(((int(length) - 50) / 250) * 150)
            command = 'pactl set-sink-volume 0 ' + str(vol) + '%'
            print(command)
            os.system(command)

    currTime = time.time()
    fps = 1 / (currTime - prevTime)
    prevTime = currTime

    cv2.putText(img, str(int(fps)), (10, 20), cv2.FONT_HERSHEY_COMPLEX, 1,
                (255, 255, 255), 1)

    cv2.imshow("Image", cv2.flip(img, 1))
    if key == ord('q'):
        cap.stop()
        break
import os
import time

import cv2
import mediapipe as mp
from MultithreadedWebcam import VideoCaptureThreading
# from imutils.video import WebcamVideoStream


class HandDetector:
    def __init__(self,
                 mode=False,
                 maxHands=2,
                 detectionConfidence=0.8,
                 trackConfidence=0.9):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionConfidence,
                                        self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findhands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList


def main():

    # cap = WebcamVideoStream(src=0).start()
    cap = VideoCaptureThreading(src=0)
    cap.start()

    prevTime = 0
    currTime = 0

    detector = HandDetector()

    while (1):
        key = cv2.waitKey(1) & 0xFF
        success, img = cap.read()
        img = detector.findhands(img)
        currTime = time.time()
        fps = 1 / (currTime - prevTime)
        prevTime = currTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (234, 0, 200), 1)

        cv2.imshow("Image", img)
        if key == ord('q'):
            cap.stop()
            break


if __name__ == "__main__":
    main()
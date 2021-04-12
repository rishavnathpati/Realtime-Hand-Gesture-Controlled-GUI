import os
import time

import cv2
import mediapipe as mp
from MultithreadedWebcam import VideoCaptureThreading
# from imutils.video import WebcamVideoStream


class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
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


def main():

    # cap = WebcamVideoStream(src=0).start()
    cap = VideoCaptureThreading()
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
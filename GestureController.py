import numpy as np
from pynput.mouse import Button, Controller
import math

mouse = Controller()

prevTime = 0
currTime = 0
sx, sy = 1920, 1080
camx, camy = 1280, 720
pinchFlag = 0
clickFlag = 0
dclickFlag = 0

mouseLocOld = np.array([0, 0])
mouseLoc = np.array([0, 0])
Dampingfactor = 4

# mouseLoc = mouseLocOld + (targetLoc - mouseLocOld) / Dampingfactor

# def volumeControl(x1, y1, x2, y2):
#     length = math.hypot(x2 - x1, y2 - y1)

#     if (length < 50):
#         cv2.circle(img, (cx12, cy12), 5, (5, 255, 2), cv2.FILLED)
#         os.system('pactl set-sink-volume 0 0')
#     else:
#         vol = int(((int(length) - 50) / 250) * 150)
#         command = 'pactl set-sink-volume 0 ' + str(vol) + '%'
#         print(command)
#         os.system(command)


def mouseControl(cx12, cy12, ch):
    global pinchFlag, clickFlag, dclickFlag, mouseLocOld, mouseLoc

    if (ch == "pointer"):  # Pointer Movement
        if (dclickFlag == 1):
            dclickFlag = 0
            mouse.release(Button.left)
        if (pinchFlag == 1):
            pinchFlag = 0
            mouse.release(Button.left)

        mouseLoc = mouseLocOld + (
            (cx12 * sx / camx, cy12 * sy / camy) - mouseLocOld) / Dampingfactor
        mouse.position = mouseLoc

        mouseLocOld = mouseLoc

    elif (ch == "click"):
        if (dclickFlag == 0):
            mouse.click(Button.left, 2)
            # mouse.release(Button.left)
            dclickFlag = 1
        if (abs(mouseLoc[0] - mouseLocOld[0]) > 5):
            mouse.click(Button.left)

    elif (ch == "drag"):  # Drag
        if (pinchFlag == 0):
            pinchFlag = 1
            mouse.press(Button.left)

        # mouseloc = (cx12 * sx / camx, cy12 * sy / camy)
        mouseLoc = mouseLocOld + (
            (cx12 * sx / camx, cy12 * sy / camy) - mouseLocOld) / Dampingfactor
        mouse.position = mouseLoc
        mouseLocOld = mouseLoc

    elif (ch == "open"):
        dclickFlag = clickFlag = 0
        mouse.release(Button.left)

    print("Finger Pos: ", cx12, cy12)
    print("Mouse Pos: ", mouse.position)
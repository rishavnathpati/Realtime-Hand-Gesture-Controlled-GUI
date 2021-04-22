import numpy as np
from pynput.mouse import Button, Controller

mouse = Controller()

sx, sy = 1920, 1080
camx, camy = 1280, 720
pinchFlag = 0
clickFlag = 0
dclickFlag = 0

mouseLocOld = np.array([0, 0])
mouseLoc = np.array([0, 0])
Dampingfactor = 5


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

    elif (ch == "click"):  # Double Click
        if (dclickFlag == 0):
            mouse.click(Button.left, 2)
            dclickFlag = 1
        if (abs(mouseLoc[0] - mouseLocOld[0]) > 5):
            mouse.click(Button.left)

    elif (ch == "drag"):  # Drag
        if (pinchFlag == 0):
            pinchFlag = 1
            mouse.press(Button.left)

        mouseLoc = mouseLocOld + (
            (cx12 * sx / camx, cy12 * sy / camy) - mouseLocOld) / Dampingfactor
        mouse.position = mouseLoc
        mouseLocOld = mouseLoc

    elif (ch == "close"):
        dclickFlag = clickFlag = 0
        mouse.release(Button.left)

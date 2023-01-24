from pynput.keyboard import Key, Controller

keybrd = Controller()


def keyboardController(ch):
    if (ch == "close"):
        # Press command + Q in mac
        keybrd.press(Key.cmd)
        keybrd.press('q')
        keybrd.release(Key.cmd)
        keybrd.release('q')

    pass

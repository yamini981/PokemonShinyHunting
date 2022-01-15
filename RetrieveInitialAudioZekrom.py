import pyautogui
import time
import librosa
import librosa.display
import matplotlib.pyplot as plt
from dtw import dtw
from numpy.linalg import norm


def A():
    pyautogui.keyDown('f5')
    time.sleep(.05)
    pyautogui.keyUp('f5')


def B():
    pyautogui.keyDown('f3')
    time.sleep(.05)
    pyautogui.keyUp('f3')


def Y():
    pyautogui.keyDown('f4')
    time.sleep(.05)
    pyautogui.keyUp('f4')


def start():
    pyautogui.keyDown('f6')
    time.sleep(.05)
    pyautogui.keyUp('f6')


def softReset():
    pyautogui.keyDown('num3')
    pyautogui.keyDown('num1')
    pyautogui.keyDown('f6')
    time.sleep(.1)
    pyautogui.keyUp('num3')
    pyautogui.keyUp('num1')
    pyautogui.keyUp('f6')


#Part 1: Enter the game
pyautogui.moveTo(2339, 25)
pyautogui.click()  # this clicks on the UCR
softReset()
time.sleep(10)
start()
time.sleep(3)
start()
time.sleep(5)
A()
time.sleep(3)
A()
time.sleep(3)

#Talk to Portal
A()
time.sleep(.8)
A()
time.sleep(.8)
A()
time.sleep(.8)
A()
A() #Final A Press before entering portal - lasts about 3 frames
time.sleep(5.95) #Waits 360 frames - total waiting of approx 363 frames

#Record Audio
pyautogui.moveTo(300, 75)
pyautogui.click()
time.sleep(1.5)  # 1.5 second recording
pyautogui.moveTo(150, 75)
pyautogui.click()
time.sleep(.1)
pyautogui.hotkey('ctrl', 'shift', 'e')
time.sleep(.3)
pyautogui.typewrite('zekromnoshinyshort1.5')  # file name
pyautogui.typewrite(['enter'])
time.sleep(.1)
pyautogui.typewrite(['enter'])
time.sleep(.1)
pyautogui.moveTo(525, 233)
pyautogui.click()
pyautogui.dragRel(-400, 0)
pyautogui.typewrite(['backspace'])
time.sleep(5)

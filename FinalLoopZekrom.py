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

count = 1746
condition = True
while condition:
    #Part 1: Enter the game
    pyautogui.moveTo(2339, 25)
    pyautogui.click()  # this clicks on the UCR
    softReset()
    time.sleep(10)
    start()
    time.sleep(3)
    start()
    time.sleep(4.5)
    A()
    time.sleep(3)
    A()
    time.sleep(4)

    #Talk to Portal
    A()
    time.sleep(.8)
    A()
    time.sleep(.8)
    A()
    time.sleep(.8)
    A()  # Final A Press before entering portal - lasts about 3 frames
    A() #extra A press - lasts about 3 frames
    time.sleep(5.95)  # Waits 357 frames - total waiting of approx 363 frames

    #Record Audio
    pyautogui.moveTo(300, 75)
    pyautogui.click()
    time.sleep(1.5)  # 1 second recording
    pyautogui.moveTo(150, 75)
    pyautogui.click()
    time.sleep(.5)
    pyautogui.hotkey('ctrl', 'shift', 'e')
    time.sleep(.5)
    pyautogui.typewrite("gameAudio" + str(count) + ".wav")  # file name
    time.sleep(.5)
    pyautogui.typewrite(['enter'])
    time.sleep(.5)
    pyautogui.typewrite(['enter'])
    time.sleep(.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(.1)
    pyautogui.typewrite(['backspace'])

    #Loading audio files
    y1, sr1 = librosa.load(
        'G:/Code/Pokemon/Zekrom/audio_files_zekrom/zekromnoshinyshort1.5.wav')
    y2, sr2 = librosa.load(
        'G:/Code/Pokemon/Zekrom/audio_files_zekrom/gameAudio' + str(count) + '.wav')

    #Showing multiple plots using subplot
    plt.subplot(1, 2, 1)
    mfcc1 = librosa.feature.mfcc(y1, sr1)  # Computing MFCC values
    librosa.display.specshow(mfcc1)

    plt.subplot(1, 2, 2)
    mfcc2 = librosa.feature.mfcc(y2, sr2)
    librosa.display.specshow(mfcc2)

    dist, cost, acc_cost, path = dtw(
        mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
    condition = dist < 5000
    count += 1
    print(str(count) + " " + str(dist))
time.sleep(5)
pyautogui.moveTo(3725, 956)
pyautogui.click()

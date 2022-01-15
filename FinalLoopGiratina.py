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

count = 7187
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
    time.sleep(6)
    A()
    time.sleep(4)
    A()
    time.sleep(4)

    #Part 2: fly to the distortion thing
    Y()
    time.sleep(1)
    A()
    time.sleep(13)
    pyautogui.keyDown('num4')
    time.sleep(1.2)
    pyautogui.keyUp('num4')
    pyautogui.keyDown('num8')
    time.sleep(.1)
    pyautogui.keyDown('f3')
    time.sleep(1.5)
    pyautogui.keyUp('num8')
    time.sleep(1)
    A()
    pyautogui.keyUp('f3')
    time.sleep(1)
    A()
    time.sleep(1)
    # Final 'a' press before flying into gap - need to wait approx 461 frames to start recording from this point, then need to record for approx
    A()
    time.sleep(6.666666667)  # approx 400 frames

    #Part 3: record audio audio should be 1.5 seconds long?
    #record button coords - x: 300 y: 75
    #stop button coords - x: 150 y: 75

    pyautogui.moveTo(300, 75)
    pyautogui.click()
    time.sleep(1.5)  # 1.5 second recording
    pyautogui.moveTo(150, 75)
    pyautogui.click()
    time.sleep(.1)
    pyautogui.hotkey('ctrl', 'shift', 'e')
    time.sleep(.4)
    pyautogui.typewrite('gameAudio' + str(count))  # file name
    pyautogui.typewrite(['enter'])
    time.sleep(.1)
    pyautogui.typewrite(['enter'])
    time.sleep(.1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(['backspace'])
    time.sleep(1)
    #Loading audio files
    y1, sr1 = librosa.load('G:/Code/audio_filesgiratina/giranoshinyshort.wav')
    y2, sr2 = librosa.load('G:/Code/audio_filesgiratina/gameAudio' + str(count) + '.wav')

    #Showing multiple plots using subplot
    plt.subplot(1, 2, 1)
    mfcc1 = librosa.feature.mfcc(y1, sr1)  # Computing MFCC values
    librosa.display.specshow(mfcc1)

    plt.subplot(1, 2, 2)
    mfcc2 = librosa.feature.mfcc(y2, sr2)
    librosa.display.specshow(mfcc2)

    dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
    condition = dist < 4200
    count += 1
    print (str(count))

time.sleep(5)
pyautogui.moveTo(3725, 956)
pyautogui.click()
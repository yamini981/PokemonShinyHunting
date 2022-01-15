import pyautogui, time

def softReset():
    pyautogui.keyDown('num3')
    pyautogui.keyDown('num1')
    pyautogui.keyDown('f6')
    time.sleep(.1)
    pyautogui.keyUp('num3')
    pyautogui.keyUp('num1')
    pyautogui.keyUp('f6')
for x in range(0,10):
    #Part 1: Enter the game
    pyautogui.moveTo(2339, 25)
    pyautogui.click()  # this clicks on the UCR
    softReset()
    time.sleep(10)
    pyautogui.typewrite(['f6'])
    time.sleep(3)
    pyautogui.typewrite(['f6'])
    time.sleep(6)
    pyautogui.typewrite(['f5'])
    time.sleep(4)
    pyautogui.typewrite(['f5'])
    time.sleep(4)

    #Part 2: fly to the distortion thing
    pyautogui.typewrite(['f4'])
    time.sleep(1)
    pyautogui.typewrite(['f5'])
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
    pyautogui.typewrite(['f5'])
    pyautogui.keyUp('f3')
    time.sleep(1)
    pyautogui.typewrite(['f5'])
    time.sleep(1)
    # Final 'a' press before flying into gap - need to wait approx 461 frames to start recording from this point, then need to record for approx
    pyautogui.typewrite(['f5'])
    time.sleep(7.33333333)  # approx 440 frames

    #Part 3: record audio audio should be 1.5 seconds long?
    #record button coords - x: 300 y: 75
    #stop button coords - x: 150 y: 75

    pyautogui.moveTo(300, 75)
    pyautogui.click()
    time.sleep(.8)  # 1.5 second recording
    pyautogui.moveTo(150, 75)
    pyautogui.click()
    time.sleep(.1)
    pyautogui.hotkey('ctrl', 'shift', 'e')
    time.sleep(.3)
    pyautogui.typewrite('giranoshinyshort' + str(x))  # file name
    pyautogui.typewrite(['enter'])
    time.sleep(.1)
    pyautogui.typewrite(['enter'])
    time.sleep(.1)
    pyautogui.moveTo(525, 233)
    pyautogui.click()
    pyautogui.dragRel(-400, 0)
    pyautogui.typewrite(['backspace'])
    time.sleep(5)

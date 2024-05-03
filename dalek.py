import time
import pyautogui

timesClicked = 0
buttonCoordinates = False

while 1:

    try:
        buttonCoordinates = pyautogui.locateOnScreen('button.png', True)
    except:
        pass

    if (buttonCoordinates):
            pyautogui.click('button.png')
            timesClicked = timesClicked + 1
            print("Click! " + str(timesClicked))

    time.sleep(15)
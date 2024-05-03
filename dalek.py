import time
import pyautogui

timesClicked = 0

buttonsToFind = [
    'button.png'
]

while 1:

    for button in buttonsToFind:
        
        buttonCoordinates = False
        print('searching for ' + str(button));

        try:
            buttonCoordinates = pyautogui.locateOnScreen(button)
        except:
            pass

        if (buttonCoordinates):
            
            x, y= pyautogui.locateCenterOnScreen(button)
            pyautogui.moveTo(x, y, duration = 0.1)
            pyautogui.leftClick()

            timesClicked = timesClicked + 1
            print('Clicking ' + str(button) + ' (' +  str(timesClicked) + ' clicks)')

    time.sleep(3)

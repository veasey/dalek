import time
import pyautogui
from random import randrange

pyautogui.FAILSAFE = False

typage = [
    '(',
    ']',
    '{',
    'a',
    'print_r',
    'cast',
    's',
    ';',
    'RepositoryInterface',
    'Class',
    'Interface',
    'Trait',
    'Abstract',
    'Exception',
    'RuntimeException',
    'there is no way a bee should be able to fly.',
    'its wings are too small to get its fat little body off the ground.',
    'The bee, of course, flies anyway',
    'because bees don’t care what humans think is impossible.',
    'Yellow, black. Yellow, black. Yellow, black. Yellow, black.',
    'Ooh, black and yellow!',
    'Let’s shake it up a little.',
    'Barry! Breakfast is ready!',
    'Ooming!',
    'Hang on a second.',
    'Hello?',
    'Barry?',
    'Adam?',
    'Can you believe this is happening?',
    'I can’t. I’ll pick you up.',
    'Looking sharp.',
    'Use the stairs. Your father paid good money for those.',
    'Sorry. I’m excited.'
]

while 1:

    startx, starty = pyautogui.position()

    time.sleep(randrange(15) + 90)

    checkx, checky = pyautogui.position()

    if startx == checkx:
        if starty == checky:

            # scroll
            toPage = randrange(2)
            if toPage == 1:
                pyautogui.press('pageup')
            if toPage == 2:
                pyautogui.press('pagedown')

            # click
            pyautogui.moveTo(56, 2125)
            pyautogui.leftClick()

            # return pos
            pyautogui.moveTo(startx, starty)


            checkx, checky = pyautogui.position()

            if startx == checkx:
                if starty == checky:

                    # type
                    if (toPage > 2):
                        interval = ((randrange(9)+1) / 10)
                        pyautogui.typewrite(typage[randrange(len(typage))], interval)




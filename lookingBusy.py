#! /usr/bin/python3


#lookingBusy.py - instant mouse movement

import pyautogui, time
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='\n')
        time.sleep(10)
        pyautogui.moveRel(30, 2, 1)
        pyautogui.moveRel(-30, -1, 1)

except KeyboardInterrupt:
        print('\nDone.')

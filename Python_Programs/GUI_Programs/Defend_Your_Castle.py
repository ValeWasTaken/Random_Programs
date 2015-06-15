'''
Automatically plays browser flash game "Defend Your Castle" 
URL: http://www.shadez1.com/defend-your-castle/
Runs in the top right-hand corner of a 1920x1080 monitor.

Note:
This was just a basic 10 minute program I made to test out the pyautogui library.
I wouldn't pay too much attention to it.
'''


import pyautogui

for game in range(100):
    for x in range(15):
        person_height = 750 
        drop_height = 320
        width = 1050

        for y in range(14):
            pyautogui.moveTo(width, height, duration=0.1)
            defender_width -= 5
            defender_height -= 5
            pyautogui.dragTo(width, drop_height, duration=0.1) # Drag to top

    # Click "OK"
    pyautogui.moveTo(1100, 755)
    pyautogui.click()

    # Repair
    pyautogui.moveTo(900, 500)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()

    # Fortify walls
    pyautogui.moveTo(900, 600)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()

    # Buy archers
    pyautogui.moveTo(1100, 520)
    pyautogui.click()
    pyautogui.click()

    # Hit "OK"
    pyautogui.moveTo(1260, 780)
    pyautogui.click()

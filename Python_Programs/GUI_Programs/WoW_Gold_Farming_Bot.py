# Work-in-progress (unfinished)

# Python 2.7
# Frostweave / gold Naxxramas farming bot - Version 0.2

import pyautogui
import time

# Start at the first step inside Naxxramas (Wrath of the Lich King raid)

def run_bot():
    pyautogui.click(800, 800)
    pyautogui.keyDown('W')
    time.sleep(2)
    
    pyautogui.keyDown('D')
    time.sleep(0.6)
    pyautogui.keyUp('D')
    
    time.sleep(4)
    pyautogui.keyDown('A')
    time.sleep(0.3)
    pyautogui.keyUp('A')
    
    time.sleep(9)
    pyautogui.keyDown('D')
    time.sleep(0.6)
    pyautogui.keyUp('D')

    time.sleep(5.5)
    pyautogui.keyDown('A')
    time.sleep(0.3)
    pyautogui.keyUp('A')
    
    time.sleep(3)
    pyautogui.keyDown('E')
    time.sleep(4e)
    pyautogui.keyUp('E')

    time.sleep(19) # Run to center of 1st boss room
    pyautogui.keyDown('A')
    time.sleep(0.5)
    pyautogui.keyUp('A')

    pyautogui.keyDown('W')
    time.sleep(14)
    pyautogui.keyUp('W')

    pyautogui.press(2) # Ice barrier
    
    pyautogui.keyDown('A')
    time.sleep(0.45)
    pyautogui.keyUp('A')

    pyautogui.keyDown('Q')
    time.sleep(1)
    pyautogui.keyUp('Q')
    
    pyautogui.press(4) # Blink

    pyautogui.keyDown('W')
    time.sleep(5)

    pyautogui.press(2) # Ice barrier
    pyautogui.keyDown('E')
    time.sleep(4.5)
    pyautogui.keyUp('E')

    time.sleep(10)
    pyautogui.keyDown('D')
    time.sleep(0.6)
    pyautogui.keyUp('D')
    
    pyautogui.keyUp('W')
    
run_bot()

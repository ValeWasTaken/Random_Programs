'''
MangaTown Scraper -- Python 3.4
Scrapes entire collections of manga saved as png files.

How to use:
Step 1: Find desired manga and go to the first page of the first chapter
    Example for "One-Punch Man" : http://www.mangatown.com/manga/onepunch_man/c001/
Step 2: Right-click the first manga picture and click "Save as.."
Step 3: Select the folder you want to download the manga to
Step 4: Run the program and wait until it is finished.

Note:
    Depending on your internet speed you may want to increase or decrease
    the time.sleep() numbers if you are unhappy with the speed or quality. 
'''
import pyautogui
import time

def scrape_manga():
    count = 1036
    while pyautogui.pixelMatchesColor(947, 550, (239, 239, 239)) == False:
        pyautogui.moveTo(947, 550)
        pyautogui.rightClick()
        time.sleep(0.4)
        save = pyautogui.locateOnScreen('SaveImageAs.png')
        x, y = [int(x) for x in str(save).replace(',','').replace('(','').split()[:2]]
        pyautogui.moveTo(x, y)
        pyautogui.click()
        s_c = str(count)
        time.sleep(1)
        pyautogui.typewrite('Page_' + '0'*(5-len(s_c)) + s_c)
        count += 1
        for x in range(10):
            pyautogui.press('enter') # Spam enter so it registers.
        pyautogui.click()
        time.sleep(1)
    print("Program is finished!")
scrape_manga()

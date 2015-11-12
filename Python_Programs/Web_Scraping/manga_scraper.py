'''
MangaTown Scraper -- Python 3.4
Scrapes entire collections of manga saved as png files.

How to use:
Step 0: Full-screen your browser on a 1920x1080 resolution monitor.
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
    count = 1 # Initalize page count
    # Check that the screen matches the color of all manga viewing pages.
    while pyautogui.pixelMatchesColor(10, 640, (23, 27, 28)) == True:
        pyautogui.moveTo(947, 550) # Move to manga page
        pyautogui.rightClick() # Right click to find "Save Image As.."
        time.sleep(0.1) # Wait 0.1 seconds for the menu containing "Save .."
        save = pyautogui.locateOnScreen('SaveImageAs.png')
        x, y = [int(x) for x in str(save).replace(',','').replace('(','').split()[:2]]
        pyautogui.moveTo(x, y) # Move to where "Save Image As.." is located.
        pyautogui.click()
        s_c = str(count)
        time.sleep(0.1)
        # Rename file to be "Page_00001"
        pyautogui.typewrite('Page_' + '0'*(5-len(s_c)) + s_c)
        count += 1
        for x in range(5):
            pyautogui.press('enter') # Spam enter so it registers.
        pyautogui.click()
        time.sleep(1.5) # Sleep while next manga page loads.
    print("Program is finished!")
scrape_manga()

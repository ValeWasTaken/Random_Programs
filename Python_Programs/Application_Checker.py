# I made this program to check my Hacker School application for updates every 15 minutes.
# I'd be lying if I said I did so for any other reason than because I could, it seemed fun,
# and so I could no longer justify spamming 'F5' a thousand times a day hoping for an update, haha.

import urllib
from bs4 import BeautifulSoup
import time

status = ''

def appScrape():
        url = 'https://www.hackerschool.com/applications/status?token=InsertYourTokenHere'
        htmlfile = urllib.urlopen(url)
        htmltext = htmlfile.read()
        soup = BeautifulSoup(htmltext)

        ans = soup.find('p')
        # ('div', {'id':'application-status-detail'}) could be used instead of 'p'
        # However, I chose 'p' because the info I wanted was the only <p> tag set.

        global status
        status = ans.string  # .string used to take out the <p> tags.

def main():
        appScrape()
        original_status = status

        while(original_status == status):
                time.sleep(900) # Wait 15 minutes between each check.
                appScrape()

        print status
        exit()
main()

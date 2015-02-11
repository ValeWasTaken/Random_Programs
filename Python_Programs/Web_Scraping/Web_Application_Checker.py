import urllib
from bs4 import BeautifulSoup
import time

status = ''

def appScrape():
        url = 'https://www.hackerschool.com/applications/status?token=InsertYourTokenHere'
        soup = BeautifulSoup(urllib.urlopen(url).read())

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

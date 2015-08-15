# Python 2.7.9 - XKCD Comic Scraper
# Downloads and saves all XKCD comics to your computer. 
# Make sure you run this within your desired XKCD picture folder!

import urllib
import re
import requests
from bs4 import BeautifulSoup

def scrapeXKCD():
    website = requests.get("http://xkcd.com/").content
    newestComicData = re.compile(r'Permanent link to this comic: http://xkcd.com/(\d+)/')
    newestComicNumber = int(newestComicData.search(website).group(1))

    for comic in range(1,newestComicNumber+1):
        if comic == 404:
            pass # 404 returns a 404 error. (Very funny, XKCD. Very funny.)
        else:
            try:
                soup = BeautifulSoup(urllib.urlopen('http://xkcd.com/%s/' % comic).read())
                title = soup.find("div", id="comic").img['alt']
                title = ''.join(char for char in title if char.isalnum() or char == ' ')
                image = "http:"+str(soup.find("div", id="comic").img['src'])
                while len(str(comic)) < len(str(newestComicNumber)):
                    comic = '0'+str(comic) # So that "1" becomes "0001" meaning your files don't go "1,10,11,..,2,20,.."
                fileName = "XKCD_{0}_{1}.jpg".format(comic, title)
                urllib.urlretrieve(image,fileName)
            except TypeError:
                pass # Some comics like #1350 and #1416 are not pictures and are interactable.
scrapeXKCD()

# Python 2.7
import urllib
from bs4 import BeautifulSoup
import time
import os

def track():
    tr = ['example1','ex2','ex3','ex4','ex5','ex6','ex7','ex8'] # tr = Tracking Number in URL
    for x in range(len(tr)):
        url = "http://webtrack.dhlglobalmail.com/?id=2720&trackingnumber="+str(tr)
        soup = BeautifulSoup(urllib.urlopen(url).read())
        statusInfo = soup.find_all("div", class_="status-info")
        for status in statusInfo:
            print("Shipment order number: "+str(x)+"\n" + status.get_text("\n", strip=True) + "\n")

def main():
    while True:
        os.system('clear')
        track()
        time.sleep(3600) # 1 hour
main()
# Screenshot of running program: https://i.imgur.com/AHiLyNw.png

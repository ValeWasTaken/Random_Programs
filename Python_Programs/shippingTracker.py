import urllib
from bs4 import BeautifulSoup
import time
import os

def track():
        urls = ["http://webtrack.dhlglobalmail.com/?id=2720&trackingnumber=<censoredForGitHub>",
                "http://webtrack.dhlglobalmail.com/?id=2720&trackingnumber=<censoredForGitHub>",
                "http://webtrack.dhlglobalmail.com/?id=2720&trackingnumber=<censoredForGitHub>",
                "http://webtrack.dhlglobalmail.com/?id=2720&trackingnumber=<censoredForGitHub>",
                "http://webtrack.dhlglobalmail.com/?id=2720&trackingnumber=<censoredForGitHub>",
                "http://webtrack.dhlglobalmail.com/?id=2720&trackingnumber=<censoredForGitHub>",
                "http://webtrack.dhlglobalmail.com/?id=2720&trackingnumber=<censoredForGitHub>",
                "http://webtrack.dhlglobalmail.com/?id=2720&trackingnumber=<censoredForGitHub>",]
        for x in range(len(urls)):
                soup = BeautifulSoup(urllib.urlopen(urls[x]).read())
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

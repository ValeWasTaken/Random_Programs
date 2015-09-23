# Python 2.7
import urllib
from bs4 import BeautifulSoup

# Finds the average amount of replies (per thread) on the first page of the Starcraft II General Discussion Forums.
def readLog():
        url = 'http://us.battle.net/sc2/en/forum/40568/'
        soup = BeautifulSoup(urllib.urlopen(url).read())

        sumOfReplies = 0
        for thread in range(43):
                replyCount = soup.findAll('td', {'class':'reply-cell'})[thread].contents[0]
                sumOfReplies += int(replyCount)
        replyAverage = (int(sumOfReplies) / 44.00)
        print("The average reply count is: %s" % replyAverage)
readLog()

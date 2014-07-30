import urllib
from bs4 import BeautifulSoup

# Finds the average amount of replies (per thread) on the first page of the Starcraft II General Discussion Forums.
def readLog():
        url = 'http://us.battle.net/sc2/en/forum/40568/'
        htmlfile = urllib.urlopen(url)
        htmltext = htmlfile.read()
        soup = BeautifulSoup(htmltext)

        sumOfReplies = 0
        thread = 0
        while(thread < 43):
                replyCount = soup.findAll('td', {'class':'reply-cell'})[thread].contents[0]
                thread += 1
                sumOfReplies += int(replyCount)
        replyAverage = (int(sumOfReplies) / 44.00) # Delete '.00' to get a whole number.
        print("The average reply count is: %s" % replyAverage)
readLog()

# Note: This program no longer works due to the 2014 Steam Summer Sale being finished.
# Python 2.7
import urllib
from bs4 import BeautifulSoup
import time
import os

def teamScores():
        url = 'http://store.steampowered.com/promotion/summer2014faq/'
        soup = BeautifulSoup(urllib.urlopen(url).read())

        blueScore = soup.findAll('div', {'title':'Blue Team'})[0].findAll('span', {'class':'score_value'})[0].contents[0]
        greenScore = soup.findAll('div', {'title':'Green Team'})[0].findAll('span', {'class':'score_value'})[0].contents[0]
        redScore = soup.findAll('div', {'title':'Red Team'})[0].findAll('span', {'class':'score_value'})[0].contents[0]
        purpleScore = soup.findAll('div', {'title':'Purple Team'})[0].findAll('span', {'class':'score_value'})[0].contents[0]
        pinkScore = soup.findAll('div', {'title':'Pink Team'})[0].findAll('span', {'class':'score_value'})[0].contents[0]

        teamScores = (blueScore, greenScore, redScore, purpleScore, pinkScore)
        currentWinner = ''
        winnerScore = max(teamScores)

        print("Steam Summer Team Scores:\n\n"
                "Blue team: %s\n"
                "Green team: %s\n"
                "Red team: %s\n"
                "Purple team: %s\n"
                "Pink team: %s\n" % teamScores)
        
        if(currentWinner == blueScore):
                print("Blue team is winning!")
        elif(currentWinner != blueScore):
                print("The current winner has %s points! Blue team is behind at %s total points." % (winnerScore, blueScore))
        else:
                print("There was an error. :(")

def main():
        while True: # Check scores once an hour
                os.system('clear')
                teamScores()
                time.sleep(3600)
main()

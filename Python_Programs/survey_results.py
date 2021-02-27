'''
This program was made to count the video game recommendations I was given.
'''

import re # For getting rid of unrequired characters.
from collections import Counter # For counting how many of each game title.

def count_games():
    # Open text file and read through it.
    with open('games_survey.txt','r') as survey:
        # Store contents in "raw_data" string.
        # .splintlines() to chunk it into full phrases / game titles
        raw_data = survey.read().splitlines()

    games = []
    for game in raw_data:
        # convert game title into all lowercase alphanumeric w/ spaces and :
        # also strip extras spaces before and after the entry.
        game = re.sub(r'[^a-zA-Z0-9 :]', '', game.lower().strip())
        games.append(game)

    # Count and list the most common game titles, one per line.
    for game, count in Counter(games).most_common():
        print('{0} had {1} requests.'.format(game, count))
        
count_games()

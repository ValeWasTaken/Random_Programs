# Searches Reddit for the shortest available names

from string import digits, ascii_lowercase
from itertools import product
import praw
import time

r = praw.Reddit(user_agent="NameFinder V0.4 by /u/valestrum")
chars = digits + ascii_lowercase
nameCount = 0

for n in range(1, 3+1): # Change 3 to be the limit of characters you want in a username.
    for comb in product(chars, repeat=n):
        username = ''.join(comb)
        #print(username) # Enable if you want to see each name being generated.
        nameCount += 1
        if nameCount % 100 == 0:
            time.sleep(30) # Used to prevent spamming Reddit too quickly with searches.
        if r.is_username_available(username) == True:
            print("USERNAME #%s IS AVAILABLE! USERNAME = %s") % (str(nameCount),username)

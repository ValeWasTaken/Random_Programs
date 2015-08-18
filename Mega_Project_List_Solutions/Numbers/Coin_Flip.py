# Python 3.4
import random

def coin_flip():
    heads, tails, count = 0, 0, 0
    flips = int(input("Number of flips: "))
    while(count < flips):
        result = random.randint(0,1)
        if result == 0:
            heads += 1
        else:
            tails += 1
        count += 1
    print("Results: {0} landed on heads. {1} landed on tails.".format(heads, tails))
coin_flip()

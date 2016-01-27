# Python 3.4
import random

def flip_coin(flips):
    heads = tails = 0
    for flip in range(flips):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print("{0} coins landed on heads. {1} landed on tails.".format(heads, tails))
flip_coin(1000)

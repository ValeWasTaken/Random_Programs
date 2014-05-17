import random

def main():
    heads = tails = count = 0 #Note: Use a,b,c = 0,1,2 format if other values.

    flips = input("How many times would you like to flip a coin? ")
    while(count < flips):
        result = random.randint(0,1)
        if (result == 0):
            heads += 1
        elif (result == 1):
            tails += 1
        else:
            print("Program error.")
        count += 1
    print("Times landed on heads: " + str(heads))
    print("Times landed on tails: " + str(tails))

main()

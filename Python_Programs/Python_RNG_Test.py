# Python RNG test
import random
    
def RNGtest():
    testNum, testRuns = 0, 100000
    fullList = [random.randint(0,9) for x in range(testRuns)]
    testRuns *= 1.0

    zero,one,two,three,four,five,six,seven,eight,nine = 0,0,0,0,0,0,0,0,0,0

    for i in fullList:
        if i == 0:
            zero += 1
        elif i == 1:
            one += 1
        elif i == 2:
            two += 1
        elif i == 3:
            three += 1
        elif i == 4:
            four += 1
        elif i == 5:
            five += 1
        elif i == 6:
            six += 1
        elif i == 7:
            seven += 1
        elif i == 8:
            eight += 1
        elif i == 9:
            nine += 1

    zeroPercent = (zero / testRuns) * 100
    onePercent = (one / testRuns) * 100
    twoPercent = (two / testRuns) * 100
    threePercent = (three / testRuns) * 100
    fourPercent = (four / testRuns) * 100
    fivePercent = (five / testRuns) * 100
    sixPercent = (six / testRuns) * 100
    sevenPercent = (seven / testRuns) * 100
    eightPercent = (eight / testRuns) * 100
    ninePercent = (nine / testRuns) * 100

    numbers = [zero,one,two,three,four,five,six,seven,eight,nine]
    percents = [zeroPercent,onePercent,twoPercent,threePercent,fourPercent,fivePercent,sixPercent,sevenPercent,eightPercent,ninePercent]

    print("Results of "+str(testRuns)+" tests of random numbers between 0 and 9.\n")
    x = 0
    while x < len(numbers):
        print(str(x)+": "+str(numbers[x])+" counts, or "+str(percents[x])+"%")
        x += 1
RNGtest()

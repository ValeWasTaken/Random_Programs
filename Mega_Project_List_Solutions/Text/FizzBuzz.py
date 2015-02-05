def fizzBuzz():
    for x in xrange(1,101):
        if x % 15 == 0:
            print("FizzBuzz!")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 3 == 0:
            print("Fizz")
        else:
            print(x)
fizzBuzz()

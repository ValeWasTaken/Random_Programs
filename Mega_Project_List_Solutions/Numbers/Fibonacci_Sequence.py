def main():
    a,b,c,fib_num,count = 0,1,0,0,0
    fib_num = input("Enter the place of the fibonacci number you want to find: ")
    while (count != fib_num):
        count += 1
        c = a + b
        print(c) # Remove this line to see only the final number.
        a = b
        b = c
    print("Your requested sequence place, %d, in the Fiboacci Sequence is: %s" % (fib_num,c))
main()

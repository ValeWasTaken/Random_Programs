def main():
    a = 0
    b = 1
    c = 0
    fib_num = 0
    count = 0

    fib_num = input("Enter the place of the fibonacci number you want to find: ")
    while (count != fib_num):
        count = count + 1
        c = a + b
        print(c) # Remove this line to see only the final number.
        a = b
        b = c
    print("Your selected number's place in the Fiboacci Sequence is: " + str(c))
main()

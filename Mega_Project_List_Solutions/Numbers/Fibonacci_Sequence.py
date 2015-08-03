a,b,c = 0,1,0
place = int(input("Enter the place of the Fibonacci number you want to find: "))
for x in range(place):
    #print(a) # -- Print the current Fibonacci number.
    c = a
    a += b
    b = c
print("Your request sequence place, {0}, in the Fibonacci Sequence is: {1}".format(place,c))

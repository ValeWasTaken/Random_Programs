'''
You have two integer arrays, a and b, and an integer target 
value v. Determine whether there is a pair of numbers, 
where one number is taken from a and the other from b, 
that can be added together to get a sum of v. Return 
true if such a pair exists, otherwise return false.
'''
def sumOfTwo(a, b, v):
    a = set(a)
    b = set(b)
    return any(v - x in b for x in a)

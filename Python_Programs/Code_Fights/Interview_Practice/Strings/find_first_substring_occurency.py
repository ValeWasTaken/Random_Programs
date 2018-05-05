'''
Implement a function that takes two strings, s and x, as arguments and 
finds the first occurrence of the string x in s. The function should return an 
integer indicating the index in s of the first occurrence of x. 
If there are no occurrences of x in s, return -1.
'''
# Python 3.6.5


def findFirstSubstringOccurrence(s, x):
    return s.find(x)
    '''
    # Less optimized alternative.
    for a in range(len(s)+1):
        if s[a:a + len(x)] == x:
            return a
    return -1
    '''

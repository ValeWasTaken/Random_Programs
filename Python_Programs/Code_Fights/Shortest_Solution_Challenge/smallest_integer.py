'''
SmallestInteger challenge in Python 3.4
Required code: 
      def SmallestInteger(matrix):
Goal: Find the lowest positive number NOT in the matrix.
Example:
  >> SmallestInteger([[1,2],[4,5]]) = 3
Solve with as few characters as possible.
Characters used in solution: 156
'''

import itertools
def SmallestInteger(m):
    t = []
    for a in itertools.chain([x for x in m]):
        t += a
    t = sorted(t)
    for n in t:
        i = n-1
        j = n+1
        if i not in t and n > 0:
            return i
        elif j not in t and n > 0:
            return j

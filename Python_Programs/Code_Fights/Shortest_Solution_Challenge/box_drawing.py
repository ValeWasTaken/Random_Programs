'''
Box drawing challenge in Python 3.4
Required code: 
      def box(n):
Goal: Create a box that made out of *s with an empty middle based on user inputted number.
Note: 0 must return '' and 1 must return '*'.
Example:
  >> 4
  >> ****
  >> *  *
  >> *  *
  >> ****
Solve with as few characters as possible.

Characters used in solution: 110
'''

def box(n):
    a = ''
    s = '*'
    b = n-2
    if n < 2:
        return {0:a,1:s}[n]
    else:
        a += s*n + '\n'
        for x in range(b):
            a += s + (b * ' ') + s +'\n'
        a += s * n
    return a

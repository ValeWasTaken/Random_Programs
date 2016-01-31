'''
Dot Product challenge in Python 3.4
Required code: 
      def Dot_product(a, b):
Goal: Find the dot product of two given arrays. ((a1*b1) + (a2*b2) + ...)
Example:
  >> Dot_product([1, 2, 3], [1, 2, 3]) = 1 + 2 * 2 + 3 * 3 = 14
Solve with as few characters as possible.
Characters used in solution: 46
'''

Dot_product = lambda a, b: sum(x*y for x,y in zip(a,b))

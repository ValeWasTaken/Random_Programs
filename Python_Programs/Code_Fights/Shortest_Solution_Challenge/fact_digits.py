'''
fact_digits challenge in Python 3.4
Required code: 
      def fact_digits(n):
Goal: Return the length of the sum of the factorial number.
Example:
  >> fact_digits(10) = 7
  >> 10! = 10*9*8*7*6*5*4*3*2*1 = 3628800 = 7 digits in length.
Solve with as few characters as possible.
Characters used in solution: 57 (using math.factorial)
'''

import math
fact_digits = lambda n: len(str(math.factorial(n)))

'''
Or if solved the long way:

def fact_digits(n):
    return len(str(int(math.sqrt(2 * math.pi * n) * (n / math.e) ** n)))
'''

'''
58 character solution that runs faster someone else cleverly made.

fact_digits = lambda n: sum(map(math.log10,range(1,n+1)),1)//1
'''

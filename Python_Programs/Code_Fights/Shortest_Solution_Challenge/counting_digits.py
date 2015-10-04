'''
counting_digits.py challenge in Python 3.4
Required code: 
      def CountingDigits(N):
Goal: Find the length of all digits side-by-side leading up to the given number.
Example:
  >> 10
  >>   -> '12345678910'
  >> Answer = 11
Solve with as few characters as possible.
Characters used in solution: 63
'''
CountingDigits = lambda N: len(''.join([str(x) for x in range(1, N+1)]))

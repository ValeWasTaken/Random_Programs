'''
nthRowSum challenge in Python 3.4
Required code: 
      def nthRowSum(n):
Goal: Find the sum of the bottom row of the pyramid given X.
Note: Pyramid format is shown here: https://codefights.com/challenge/nMYyfjyQQmeoogjEQ
Example:
  >> 4
  >>     1
  >>    232
  >>   34543
  >>  4567654 = 4+5+6+7+6+5+4 = 37
Solve with as few characters as possible.
Characters used in solution: 45
'''
nthRowSum = lambda n: sum(range(n,n*2-1))*2 + n*2-1

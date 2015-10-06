'''
Palindromic_Number challenge in Python 2.7
Required code: 
      def Palindromic_Number(N):
Goal: Given a number, return the numbers leading up to it as a palindrome.
Note: The final number should only be used once in the middle.
Example:
  >> 5
  >>   -> '123454321'
  >> 8
  >>   -> '123456787654321'
Solve with as few characters as possible.
Characters used in solution: 69
'''

Palindromic_Number = lambda N: ''.join(map(str, range(1,N) + range(N,0,-1)))

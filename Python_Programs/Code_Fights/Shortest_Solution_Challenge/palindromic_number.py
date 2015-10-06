'''
Palindromic_Number challenge in Python 3.4
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
Characters used in solution: 76
'''

def Palindromic_Number(N):
    a = ''
    for x in range(1,N+1):
        a += str(x)
    return a + a[::-1][1:]

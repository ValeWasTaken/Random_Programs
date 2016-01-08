'''
isBinSymmetry challenge in Python 3.4
Required code: 
      def isBinSymmetry(x):
Goal: Given a decimal number, determine if its binary form is a palindrome.
Note: Single digits (Ex: '1') are not counted as palindromes.
Example:
  >> x = 99
  >> 99 = 1100011 in binary. 1100011 is a palindrome.
  >> True
  >> x = 11
  >> 11 = 1011 in binary. 1011 != 1101, not a palindrome.
  >> False
Solve with as few characters as possible.
Characters used in solution: 54
'''

def isBinSymmetry(x):
    b = bin(x)[2:]
    return x > 9 and b == b[::-1]

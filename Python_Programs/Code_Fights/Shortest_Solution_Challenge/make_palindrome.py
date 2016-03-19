
'''
Make Palindrome challenge in Python 3.4
Required code: 
      def makePalindrome(s):
Goal: Determine if you can create a palindrome using a given string.
Note: xzyzx would be considered a palindrome.
Example:
  >> makePalindrome("xyyx") == True
  >> makePalindrome("abcde") == False
Solve with as few characters as possible.
Characters used in solution: 50
'''
makePalindrome = lambda s: all([s.count(x) == 2 for x in s])

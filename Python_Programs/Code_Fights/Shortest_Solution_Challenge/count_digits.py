'''
count_digits challenge in Python 3.4
Required code: 
      def CountDigits(string):
Goal: Count how many numbers are within the string.
Example:
  >> CountDigits('N3V3RG!V3UPS0N') = 4
  >> There are 4 digits in the string.
Solve with as few characters as possible.
Characters used in solution: 43
'''
CountDigits = lambda s: sum(c.isdigit() for c in s)

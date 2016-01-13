'''
hexadecimal challenge in Python 3.4
Required code: 
      def hexadecimal(n):
Goal: Convert the number string into hexidecimal format.
Example:
  >> hexadecimal(47156) = "B834"
  >> hexadecimal(41574) = "A266"
Solve with as few characters as possible.
Characters used in solution: 28
'''
hexadecimal = lambda n: '%04X' % n

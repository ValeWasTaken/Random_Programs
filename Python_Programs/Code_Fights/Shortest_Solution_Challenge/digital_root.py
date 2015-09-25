'''
digital_root challenge in Python 3.4
Required code: 
      def digitalroot(n):
Goal: Find the digital root of the number. (Sum of all digits)
Note: The number is given as a string.
Example:
  >> 999
  >> 9 + 9 + 9 = 27
  >> 2 + 7 = 9
  >> 9
Solve with as few characters as possible.
Characters used in solution: 75
'''
def digitalroot(n):
    while len(str(n)) > 1:
        n = sum([int(x) for x in str(n)[::]])
    return n

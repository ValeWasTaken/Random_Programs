'''
LastPower challenge in Python 3.4
Required code: 
      def LastPower(a, b):
Goal: Return the last digit of a^b
Example:
  >> LastPower(2, 4)
  >> 2 * 2 * 2 * 2 = 16
  >> 6
Solve with as few characters as possible.
Characters used in solution: 53
'''
LastPower = lambda a, b: int(str(int(math.pow(a, b)))[-1:])

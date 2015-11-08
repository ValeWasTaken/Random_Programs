'''
Triangle challenge in Python 3.4
Required code: 
      def Triangle(n):
Goal: Return the largest angle of a triangle given 2 angles.
Example:
  >> Triangle(30, 80)
  >> 80
Solve with as few characters as possible.
Characters used in solution: 35
'''

Triangle = lambda a, b: max(a, b, 180 - a - b)

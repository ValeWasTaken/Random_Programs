'''
Find the Single Value challenge in Python 3.4
Required code: 
      def FindTheSingleValue(arr):
Goal: Find the only value used only once in the array.
Example:
  >> FindTheSingleValue([1,4,2,6,4,6,2, 4]) = 1
Solve with as few characters as possible.
Characters used in solution: 54
'''

FindTheSingleValue = lambda a: [x for x in a if a.count(x) < 2][0]

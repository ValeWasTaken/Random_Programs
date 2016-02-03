'''
smallest_negative challenge in Python 3.4
Required code: 
      def smallestNegative(A):
Goal: Given an array of numbers find the smallest negative number. If there are no negatives return "NOT_FOUND"
Example:
  >> smallestNegative([1,2,3]
  >> "NOT_FOUND"
  >> smallestNegative([5,-2,-3]
  >> "-3"
Solve with as few characters as possible.
Characters used in solution: 61
'''

smallestNegative = lambda A: str(min(A)) if min(A) < 0 else 'NOT_FOUND'

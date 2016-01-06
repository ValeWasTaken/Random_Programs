'''
integerAverage challenge in Python 3.4
Required code: 
      def integerAverage(a):
Goal: Determine if the average value of an array is an integer.
Example:
  >> [1, 2, 3] -> 6 / 3 = 2 -> 2 is an int()
  >> True
  >> [1, 2, 2] -> 5 / 3 = 1.6666 -> 1.666 is NOT an int()
  >> False
Solve with as few characters as possible.
Characters used in solution: 46
'''
integerAverage = lambda a: sum(a)/(len(a)+.0) % 1 == 0

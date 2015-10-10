'''
Triangular_Numbers challenge in Python 3.4
Required code: 
      def triangular_numbers(n):
Goal: Given a number of layers in a 2D triangle, find the # of stars / blocks.
Example:
  >> 3
  >>   ->    *
  >>   ->   * *
  >>   ->  * * *
  >>   -> Answer: 6
Solve with as few characters as possible.
Characters used in solution: 36
'''

triangular_numbers = lambda n: n*(n+1)/2

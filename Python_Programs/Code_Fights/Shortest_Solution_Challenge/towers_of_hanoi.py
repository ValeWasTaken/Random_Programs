'''
towers_of_hanoi challenge in Python 3.4
Required code: 
      def towers_of_hanoi(n):
Goal: Find the optimal amount of moves needed to solve the tower of hanoi.
Example:
  >> towers_of_hanoi(1) = 1
  >> towers_of_hanoi(2) = 3
Solve with as few characters as possible.
Characters used in solution: 30
'''
towers_of_hanoi = lambda n: 2**n-1

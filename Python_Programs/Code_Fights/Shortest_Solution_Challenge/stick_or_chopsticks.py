'''
Stick Or Chopsticks challenge in Python 3.4
Required code: 
      def StickOrChopsticks(thing, n):
Goal: Find the number of chopsticks or sticks given the other.
Note: You must return -1 if there is a leftover stick.
Example:
  >> StickOrChopsticks("stick",10) = 5
  >> StickOrChopsticks("stick",11) = -1
  >> StickOrChopsticks("chopstick",5) = 10
Solve with as few characters as possible.
Characters used in solution: 49
'''
StickOrChopsticks = lambda s, n:[n%-2|n/2,n*2][s<"d"]

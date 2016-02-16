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
Characters used in solution: 62
'''
StickOrChopsticks = lambda t, n: n*2 if len(t)>6 else n/2 if n%2==0 else -1

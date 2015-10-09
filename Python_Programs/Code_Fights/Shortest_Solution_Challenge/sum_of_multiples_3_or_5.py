'''
Sum_Of_Multiples_3_Or_5 challenge in Python 3.4
Required code: 
      def Sum_Of_Multiples_3_Or_5(N):
Goal: Find the sum of all numbers divisable by 3 and/or 5 under N.
Example:
  >> N = 10 -> 3 + 5 + 6 + 9 = 23
Solve with as few characters as possible.
Characters used in solution: 70
'''
Sum_Of_Multiples_3_Or_5 = lambda N: sum([x for x in range(N) if x % 3 == 0 or x % 5 == 0])

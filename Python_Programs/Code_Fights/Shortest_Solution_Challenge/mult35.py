'''
Mult35 challenge in Python 3.4
Required code: 
      def mult35(N):
Goal: Return the sum of all numbers under N divisable by 3 or 5.
Note: Solution must be returned as a string and can handle N = 10^9
Example:
  >> mult35(20) = "78"
  >> 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78
Solve with as few characters as possible.
Characters used in solution: 58
'''

mult35 = lambda N: str(sum([x for x in range(N) if x % 3 == 0 or x % 5 == 0]))

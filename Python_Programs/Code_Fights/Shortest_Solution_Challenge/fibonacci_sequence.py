'''
Fibonaaci sequence challebge in Python 3.4
Required code: 
      def Fib(n):
Goal: Generate the Nth number in the fibonacci sequence.
Note: You must return your answer modulo by 10**9+7.
Example:
  >> Input: 6
  >> Output: 5
  
  >> Input: 51
  >> Output: 586268941
Solve with as few characters as possible.
Characters used in solution: 59
'''

def Fib(N):
    a = 0
    b = 1
    for x in range(N-1):
        a, b = b, a+b
    return a % (10**9+7)

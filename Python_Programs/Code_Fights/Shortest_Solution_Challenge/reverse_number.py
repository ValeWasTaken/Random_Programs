'''
reverse_number challenge in Python 3.4
Required code: 
      def reverse_number(n):
Goal: Find the reverse of a number.
Note: If there are leading zeroes they are excluded from the answer.
Example:
  >> 6587 -> 7856
  >> 20   -> 2
Solve with as few characters as possible.
Characters used in solution: 40
'''
reverse_number = lambda n: int(str(n)[::-1])

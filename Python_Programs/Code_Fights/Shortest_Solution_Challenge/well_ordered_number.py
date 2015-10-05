'''
well_ordered_number challenge in Python 3.4
Required code: 
      def wellOrderedNumber(n):
Goal: Check if the number given increases with each digit.
Example:
  >> 1234
  >>   -> True
  >> 1723
  >>   -> False
Solve with as few characters as possible.
Characters used in solution: 71
'''

def wellOrderedNumber(n):
    p = 0
    for x in str(n):
        x = int(x)
        if x <= p:
            return False
        p = x
    return True

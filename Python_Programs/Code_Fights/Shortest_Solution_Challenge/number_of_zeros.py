'''
number_of_zeros challenge in Python 3.4
Required code: 
      def NumberofZeros(n):
Goal: Count the number of trailing zeros in N!
Note: Solution unoptimized, improve later.
Example:
  >> 5!
  >> = 5 * 4 * 3 * 2 * 1
  >> = 120
  >> = 1 trailing zero
Solve with as few characters as possible.
Characters used in solution: 93
'''
def NumberofZeros(n):
    a = 1
    for x in range(1, n+1):
        a *= x
        
    z = 0
    for c in str(a)[::-1]:
        if c == '0':
            z += 1
        else:
            return z

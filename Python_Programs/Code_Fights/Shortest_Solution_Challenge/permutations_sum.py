'''
permutations_sum challenge in Python 3.4
Required code: 
      def permutations_sum(n):
Goal: Return the sum of all permutations excluding leading zeroes of a given number.
Example:
  >> permutations_sum(123)
  >> 123 + 132 + 231 + 312 + 213 + 321 = 1332
Solve with as few characters as possible.
Characters used in solution: 116
'''

import itertools
permutations_sum = lambda n: sum([int(x) for x in set(list(''.join(p) for p in itertools.permutations(str(n))))])

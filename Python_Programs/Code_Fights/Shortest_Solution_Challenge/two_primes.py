'''
two_primes challenge in Python 3.4
Required code: 
      def two_primes(a, b):
Goal: Given two numbers, check if both are prime.
Example:
  >> 9, 7
  >>   -> False
  >> 3, 7
  >>   -> True
Solve with as few characters as possible.
Characters used in solution: 87
'''
p = lambda n: all([(n%j) for j in range(2, int(n**0.5)+1)]) and n>1
TwoPrimes = lambda a, b: p(a) and p(b)

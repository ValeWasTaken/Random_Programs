'''
Box drawing challenge in Python 3.4
Required code: 
      def Chocolates(B, w):
Goal: Pelnin buys Chocolates from a Shop. He gets one extra chocolate for every w Chocolate wrappers
that he gives to the shopkeeper. Now Pelnin is worried because he made an error in calculating
how many Chocolates he will get, having B bucks in the pocket. 
Help him out to find how many Chocolates he can get.

Note:
  - Pelnin has 0 Chocolate wrappers at the beginning.
  - Pelnin has B bucks in his pocket
  - Shopkeeper has infinite Chocolates.
  - One Chocolate costs 1 buck, or w Chocolate wrappers.

Example :
  - For B = 25 and w = 3 the output should be 37.
  - For B = 123123 and w = 7 the output should be 143643.
  - For B = 8932434 and w = 22 the output should be 9357787.

Solve with as few characters as possible.
Characters used in solution: 69
'''

def Chocolates(B, w):
  t = c = r = B
  while r >= w:
    c = 0
    c += int(r / w)
    t += c
    r %= w
    r += c
  return t
  
# Reference
# ---------------------------------
# t = total chocolates
# c = temporary chocolates
# B = bucks
# r = wrappers
# w = Cost of wrapper to chocolate

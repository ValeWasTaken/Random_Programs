'''
bear_pyramid challenge in Python 3.4
Required code: 
      def bear_pyramid(N):
Goal: Fight the height of the largest teddy bear pyramid Justin can make.
Note: Teddy bear height is 3 + 1 for the head at the top of the pyramid.
Example:
  >> 6
  >>   * 3 + 1
  >>  * * + 3
  >> * * * + 3
  >> Height = 10
Solve with as few characters as possible.
Characters used in solution: 85
'''
def bear_pyramid(N):
    if N <= 0:
        return 0
    c = m = 0
    h = 1
    for x in range(N+1):
        if c > m:
            m = c
            c = 0
            h += 3
        c += 1
    return h

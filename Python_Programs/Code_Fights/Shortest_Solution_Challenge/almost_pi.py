'''
Almost Pi challenge in Python 3.4
Required code: 
      def almostPi(n):
Goal: Return the percentage of how close to pi a number is.
Note: You must format it as "XX.XX%"
Example:
  >> almostPi(3.05) --> "97.08%"
  >> almostPi(0.06) --> "1.91%"
Solve with as few characters as possible.
Characters used in solution: 43
'''
almostPi = lambda n: '%.2f' % (n*100 / math.pi) + '%'

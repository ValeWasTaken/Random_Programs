'''
dice_probability challenge in Python 3.4
Required code: 
      def diceProbability(d1, d2, N):
Goal: Given 2 die consisting of sides d1 and d2, find the sum of sides within d1 and d2 that can equal N.
Example:
  >> Input: [[1,2][1,2],3]
  >> Output: 2
Solve with as few characters as possible.
Characters used in solution: 66
'''
def diceProbability(d1, d2, N):
    return len([x for x in d1 for y in d2 if x+y==N])

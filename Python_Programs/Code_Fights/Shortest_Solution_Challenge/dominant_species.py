'''
dominant_species challenge in Python 3.4
Required code: 
      def dominant_species(A):
Goal: Find the most common number in a list.
Example:
  >> [1,2,1,3,3,1,0,1,1,9,1]
  >> 1
Solve with as few characters as possible.
Characters used in solution: 43
'''
Dominant_species = lambda A: max(A, key=A.count)

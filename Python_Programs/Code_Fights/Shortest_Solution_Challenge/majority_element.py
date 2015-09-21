'''
majority_element challenge in Python 3.4
Required code: 
      def Majority_Element(N, array):
Goal: Given an array, find the number that appears more than half the time.
Note: If there is no such number, return -1.
Example:
  >> [3,3,4,2,4,4,2,4,4]
  >> 4
Solve with as few characters as possible.
Characters used in solution: 98
'''
def Majority_Element(N, array):
    a = array
    m = max(set(a), key=a.count)
    if a.count(m) > len(a) / 2:
        return m
    return -1

'''
sum_groups challenge in Python 3.4
Required code: 
      def SumGroups(a):
Goal: Given an array of integers, sum consecutive even numbers and consecutive odd-numbers. 
Repeat the process while it can be done and return the length of the final array.
Example:
  >> arr = [2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]
  >> [2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]  -->
  >> [2, 1, 10, 5, 2, 24, 4, 15] -->
  >> [2, 1, 10, 5, 30, 15]  - array of length 6
Solve with as few characters as possible.
Characters used in solution: N/A -- Not my solution, just a clever one I saw and wanted to remember.
'''
def SumGroups(a):
  l = 1
  for x in a[1:]:
    x %= 2
    l += (a[0] + l + ~x) % 2 * -~x - x
  
  return l

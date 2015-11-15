'''
sum_of_consecutive_numbers challenge in Python 3.4
Required code: 
      def SumOfConsecutiveNumbers(numArray):
Goal: Return the sum of all consecutive numbers within the array.
Example:
  >> SumOfConsecutiveNumbers((1,2,3,4,6,8,9))
  >> 1 + 2 + 3 + 4 + 8 + 9 = 27
  >> SumOfConsecutiveNumbers((1,1,1,1))
  >> 0
Solve with as few characters as possible.
Characters used in solution: 126
'''

def SumOfConsecutiveNumbers(numArray):
    s = 0
    a = numArray
    for d in range(len(a)):
        try:
            n = a[d]
            if n - a[d-1] == 1 or a[d+1] - n == 1:
                s += n
        except:
            0
    return s
    
'''
Note
There is a shorter way to write this program using around 98 characters but 
I felt the program wasn't worth the extra effort as it was ranked lowly on
CodeFights. However I believe the 98 char solution would look something like
SumOfConsecutiveNumbers = lambda numArray: [for d in range(len(a))] if if n - a[d-1] == 1 or a[d+1] - n == 1: sum += a[d]

'''
Average of 5 challenge in Python 3.4
Required code: 
      def aofive(t):
Goal: Remove the highest and lowest number of 5 and then find the average number.
Note: You must submit the answer rounded to 2 decimal places.
Example:
  >> aofive([17.87, 19.86, 19.46, 17.25, 23.16])
  >> 17.25 and 23.16 are removed.
  >> (17.87 + 19.46 + 19.86) / 3 = 19.063333333333333
  >> 19.063333333333333 = 19.06
  >> 19.06
Solve with as few characters as possible.
Characters used in solution: 46
'''
aofive = lambda t: round(sum(sorted(t)[1:-1]) / 3, 2)

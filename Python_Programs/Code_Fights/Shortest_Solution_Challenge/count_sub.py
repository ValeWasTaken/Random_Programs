'''
CountSub challenge in Python 3.4
Required code: 
      def countSub(sup, sub):
Goal: Count the number of times the string sub appears within the string sup.
Note: Overlapping occurences should count!
Example:
  >> countSub("abcdefga", "a") = 2
  >> countSub("aaa", "aa") = 2
Solve with as few characters as possible.
Characters used in solution: 72
'''
countSub = lambda sup, sub: sum(sup[i:].startswith(sub) for i in range(len(sup)))

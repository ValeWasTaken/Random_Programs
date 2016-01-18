'''
PressButton challenge in Python 3.4
Required code: 
      def PressButton(s, n):
Goal: Given a binary number and the amounts of switches it makes determine
what the returned number is.
Example:
  >> PressButton(1, "1") = 0
  >> PressButton(0, "0") = 0
  >> PressButton(1, "10") = 1
Solve with as few characters as possible.
Characters used in solution: 32
'''
PressButton = lambda s, n: s ^ int(n) % 2

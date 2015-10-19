'''
virus_scan challenge in Python 3.4
Required code: 
      def virusScan(input):
Goal: Detect if the string 'virus' is contained within the given string, regardless of letter case.
Example:
  >> 'thisIsAviRuS'
  >> True
Solve with as few characters as possible.
Characters used in solution: 36
'''
virusScan = lambda n: 'virus' in n.lower()

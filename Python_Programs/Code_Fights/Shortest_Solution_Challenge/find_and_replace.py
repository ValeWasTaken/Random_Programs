'''
find_and_replace challenge in Python 3.4
Required code: 
      def findAndReplace(originalString, stringToFind, stringToReplace):
Goal: Replace the substrings within a string with a different string.
Example:
  >> findAndReplace("I love Codefights", "I", "We")
  >>   -> '"We love Codefights"'
Solve with as few characters as possible.
Characters used in solution: 41
'''
findAndReplace = lambda A,B,C: A.replace(B,C)

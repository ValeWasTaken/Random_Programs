'''
DecorateComment challenge in Python 3.4
Required code: 
      def DecorateComment(cmt):
Goal: Decorate the comment string provided as shown below.
Example:
  >> "This is my comment"
  >> ..
  >>  ["////////////////////////",
  >>   "// This is my comment //", 
  >>   "////////////////////////"]
Solve with as few characters as possible.
Characters used in solution: 57
'''
def DecorateComment(c):
    a="// %s //"%c
    b="/"*len(a)
    return b,a,b

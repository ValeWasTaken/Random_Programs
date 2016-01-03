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
Characters used in solution: 62
'''
def DecorateComment(c):
    e = [(6+len(c)) * '/']
    return e+['// %s //' % c]+e

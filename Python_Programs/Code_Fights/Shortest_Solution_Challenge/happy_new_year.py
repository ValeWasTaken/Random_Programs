'''
happy_new_year challenge in Python 3.4
Required code: 
      def happyNewYear(s):
Goal: Return a "Happy New Year" message framed with *s.
Example:
  >> happyNewYear(s) = ['*************', 
                      '* Happy     *', 
                      '* New       *', 
                      '* Year      *', 
                      '* and       *', 
                      '* CodeFight *', 
                      '* On        *', 
                      '* in        *', 
                      '* 2016!     *', 
                      '*************']
Solve with as few characters as possible.
Characters used in solution: 117
'''
def happyNewYear(s):
    w = [x for x in s.split()]
    l = max(len(x) for x in w)
    e = ['*' * (l+4)]
    return e+['* %s%s *' % (x, ' '*(l-len(x))) for x in w]+e

'''
Replace Words challenge in Python 3.4
Required code: 
      def replaceWords(sentence):
Goal: Replace the 1st, 2nd, 3rd, .. longest words with the 1st, 2nd, 3rd, .. shortest words.
Note: You must use correct capitalization. (The word "I" is uppcased and only the first letter
       of the first word can also be capitalized.)
Example:
  >> sentence: "I am the best"
  >> "Best the am I"
Solve with as few characters as possible.
Characters used in solution: 164
'''

def replaceWords(s):
    s = s.lower().split()
    o = sorted(s, key=len)
    r = o[::-1]
    a = []
    for w in s:
        a.append(r[o.index(w)])
    a = ['I' if i=='i' else i for i in a]
    a = ' '.join(a)
    return a[0].upper() + a[1:]

'''
pig_latin challenge in Python 3.4
Required code: 
      def piglatin(word):
Goal: Convert words into their Pig Latin translation.
Note: Pig Latin explanations can be found via Google or Wikipedia.
Example:
  >> 'amazing'
  >>   -> 'amazingway'
  >>  'flywhy'
  >>   -> 'ywhyflay'
Solve with as few characters as possible.
Characters used in solution: 112
'''
def piglatin(word):
    w = word
    v = 'aeiouy'
    if w[:1] in v:
        return w + 'way'
    for c in range(len(w)):
        if w[c] in v:
            return(w[c:] + w[:c] + 'ay')

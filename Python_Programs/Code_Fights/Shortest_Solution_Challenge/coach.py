'''
Coach challenge in Python 3.4
Required code: 
      def Coach(N, players):
Goal: Return the first letter of all surnames shared by at least 5 surnames.
Note: The answer must be sorted alphabetically.
Example:
  >> Coach(N, players) where N = 18 and
  >> players = ["babic","keksic","boric","bukic",
           "sarmic","balic","kruzic","hrenovkic",
           "beslic","boksic","krafnic","pecivic",
           "klavirkovic","kukumaric","sunkic","kolacic",
           "kovacic","prijestolonasljednikovic"]
  >> Coach(N, players) = "bk"
Solve with as few characters as possible.
Characters used in solution: 131
'''

import collections

def Coach(N, t):
    f = collections.Counter([p[0] for p in t])
    a = ''.join(sorted([k for k in f if f[k] > 4]))
    return 'forfeit' if a == '' else a

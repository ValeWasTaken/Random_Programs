# Python 3.4

# One-liner solution
vowel_count = lambda s: sum(1 for c in s if c in 'aeiouAEIOU')

# Added complexity solution
from collections import Counter

def vowel_count(s):
    count = Counter([c for c in s.lower()[::]])
    a = [count[vowel] for vowel in 'aeiou']
    return 'A: {0}, E: {1}, I: {2}, O: {3}, U: {4}'.format(a[0],a[1],a[2],a[3],a[4])

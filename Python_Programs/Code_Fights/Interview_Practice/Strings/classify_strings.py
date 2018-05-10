'''
You categorize strings into three types: good, bad, or mixed. 
If a string has 3 consecutive vowels or 5 consecutive consonants, 
or both, then it is categorized as bad. Otherwise it is 
categorized as good. Vowels in the English alphabet are 
["a", "e", "i", "o", "u"] and all other letters are consonants.

The string can also contain the character ?, which can be 
replaced by either a vowel or a consonant. This means that the 
string "?aa" can be bad if ? is a vowel or good if it 
is a consonant. This kind of string is categorized as mixed.

Implement a function that takes a string s and 
returns its category: good, bad, or mixed.

Disclaimer: This one actually wasn't my solution. Originally I was 
trying to do it without regex by converting characters to numbers 
(0, 1, 2) and using if statements, but some edge cases made it 
unreasonable. I ended up posting this solution here because I 
understand it and am interested in referencing it in the future.
'''
# Python 3.6.5
def classifyStrings(s):
    if re.findall('(([aeiou]{3})|[^aeiou?]{5})',s):
        return 'bad'
    if '?' in s:
        a = classifyStrings(s.replace('?','a',1))
        b = classifyStrings(s.replace('?','n',1))
        return a if a == b else 'mixed'
    return 'good'

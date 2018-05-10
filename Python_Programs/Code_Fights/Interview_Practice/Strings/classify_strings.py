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
'''
# Python 3.6.5

def classifyStrings(s):
        chars = 'bcdfghjklmnpqrstvwxyzaeiou?'
        numbers = '000000000000000000000111112'
        chars_to_nums = ''.maketrans(chars, numbers)
        translation = s.translate(chars_to_nums)
        
        if len(s) < 3:
                return 'good'
        
        for a in range(len(s)+1):
            value = translation[a:a+3]
            if '2' in value:
                return 'mixed'
            elif value == '111' or value == '222':
                return 'bad'
        return 'good'

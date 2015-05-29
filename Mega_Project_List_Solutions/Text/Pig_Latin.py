# Python 3.4

def pig_latin(word):
    vowels = 'aeiouy'
    new_word = []
    if word[:1] not in vowels:
        word = word[1:] + word[:1] + 'ay'
    else:
        word += 'way'
    print(word)
pig_latin(input())

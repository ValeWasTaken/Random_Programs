# Python 3.4
def encode_cipher(message, key):
    answer = []
    temp = [ord(character) for character in message]
    for number in temp:
        number = int(number)
        number += key # shift number value by key value.
        if number > 122:
            number += 26
        answer.append(chr(number)) # Convert back into letter.
    return ''.join(answer)

def decode_cipher(message, key):
    answer = []

    # Convert letter into number value.
    temp = [ord(character) for character in message]
    for number in temp:
        number = int(number)
        number -= key # shift number value by key value.
        if number < 65:
            number += 26
        answer.append(chr(number)) # Convert back into letter.
    return ''.join(answer)
    
'''
Examples:

print(encode_cipher("Abcdefg", 2)) # Output: Cdefghi
print(decode_cipher('def', 3))     # Output: abc
print(decode_cipher(encode_cipher("Abcdefg", 2), 2)) # Abcdefg
'''

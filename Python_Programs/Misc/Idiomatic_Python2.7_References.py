# Example 1: Avoid repeating variable name in compound if statement
# -- Harmful --
is_generic_name = False
name = 'Tom'
    if name == 'Tom' or name == 'Dick' or name == 'Harry':
        is_generic_name = True

# -- Idiomatic--
name = 'Tom'
is_generic_name = name in ('Tom', 'Dick', 'Harry')



# Example 2: Use if and else as a short ternary operator replacement
# -- Harmful --
foo = True
value = 0

if foo:
    value = 1
print(value)

# -- Idiomatic -- 
foo = True
value = 1 if foo else 0
print(value)



# Example 3: Use the in keyword to iterate over an iterable
# -- Harmful --
my_list = ['Larry', 'Moe', 'Curly']
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
    
# -- Idiomatic --
my_list = ['Larry', 'Moe', 'Curly']
for element in my_list:
    print(element)



# Example 4: Use else to execute code after a for loop concludes
# -- Harmful --
for user in get_all_users():
    has_malformed_email_address = False
    print('Checking {}'.format(user))
    
for email_address in user.get_all_email_addresses():
    if email_is_malformed(email_address):
        has_malformed_email_address = True
        print('Has a malformed email address!')
        break
    if not has_malformed_email_address:
        print('All email addresses are valid!')

# -- Idiomatic --
for user in get_all_users():
    has_malformed_email_address = False
    print('Checking {}'.format(user))
    
for email_address in user.get_all_email_addresses():
    if email_is_malformed(email_address):
        has_malformed_email_address = True
        print('Has a malformed email address!')
        break
    else:
        print('All email addresses are valid!')
        
        
        
# Example 5: Avoid using a mutable object as the default value for a function argument
# -- Harmful --
def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) # [1]
print(f(2)) # [1, 2]
print(f(3)) # [1, 2, 3]

# -- Idiomatic --
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1)) # [1]
print(f(2)) # [2]
print(f(3)) # [3]



# Example 6: Use return to evaluate expressions in addition to return values
# -- Harmful --
def all_equal(a, b, c):
    result = False
    if a == b == c:
        result = True
    return result

# -- Idiotmatic --
def all_equal(a, b, c):
    return a == b == c # If a == b == c isn't true it will return False



# Example 6: Learn to treat functions as values
# -- Harmful --
def print_addition_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x + y) + '\n')
def print_subtraction_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x - y) + '\n')
def print_multiplication_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x * y) + '\n')
def print_division_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x / y) + '\n')
print_addition_table()
print_subtraction_table()
print_multiplication_table()
print_division_table()

# -- Idiomatic --
import operator as op
print "test"

def print_table(operator):
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(operator(x, y)) + '\n')
            
for operator in (op.add, op.sub, op.mul, op.div):
    print_table(operator)



# Example 8: Use Exceptions to Write Code in "EAFP" Style (Easier to ask forgiveness than for permission)
# -- Harmful --
def get_log_level(config_dict):
    if 'ENABLE_LOGGING' in config_dict:
        if config_dict['ENABLE_LOGGING'] != True:
            return None
        elif not 'DEFAULT_LOG_LEVEL' in config_dict:
            return None
        else:
            return config_dict['DEFAULT_LOG_LEVEL']
    else:
        return None

# -- Idiomatic --
def get_log_level(config_dict):
    try:
        if config_dict['ENABLE_LOGGING']:
            return config_dict['DEFAULT_LOG_LEVEL']
    except KeyError:
    # if either value wasn't present,
    # a KeyError will be raised, so return None
    return None



# Example 9: Use ord to get the ASCII code of a character and ord to get the character from an ASCII code.
# -- Harmful --
hash_value = 0
character_hash = {
    'a': 97,
    'b': 98,
    'c': 99,
    # ...
    'y': 121,
    'z': 122,
    }
for e in some_string:
    hash_value += character_hash[e]
return hash_value

# -- Idiomatic --
hash_value = 0
for e in some_string:
    hash_value += ord(e)
return hash_value



# Example 10: Prefer the format function for formatting strings
# -- Harmful --
def get_formatted_user_info_worst(user):
    # Tedious to type and prone to conversion errors
    return 'Name: ' + user.name + ', Age: ' + \
        str(user.age) + ', Sex: ' + user.sex

def get_formatted_user_info_slightly_better(user):
    # No visible connection between the format string placeholders
    # and values to use. Also, why do I have to know the type?
    # Don't these types all have __str__ functions?
    return 'Name: %s, Age: %i, Sex: %c' % (user.name, user.age, user.sex)

# -- Idiotmatic --
def get_formatted_user_info(user):
    # Clear and concise. At a glance I can tell exactly what
    # the output should be. Note: this string could be returned
    # directly, but the string itself is too long to fit on the page.
    output = 'Name: {user.name}, Age: {user.age}, Sex: {user.sex}'.format(user=user)
    return output



# Example 11: Make use of negative indexes.
# -- Harmful --
def get_suffix(word):
    word_length = len(word)
    return word[word_length - 2:]

# -- Idiotmatic --
def get_suffix(word):
    return word[-2:]



# Example 12: Prefer xrange to range unless you need the resulting list
# (xrange doesn't store the entire list in memory)

# -- Harmful --
# A loop over a large range that breaks out
# early: a double whammy!
even_number = int()
for index in range (1000000):
    if index % 2 == 0:
        even_number = index
        break

# -- Idiotmatic --
even_number = int()
for index in xrange(1000000):
    if index % 2 == 0:
        even_number = index
        break



# Example 14: Document what something does, not how.
# -- Harmful --
def is_prime(number):
        """Mod all numbers from 2 -> number and return True
        if the value is never 0"""
        for candidate in range(2, number):
                if number % candidate == 0:
                        print(candidate)
                        print(number % candidate)
                        return False
        return number > 0

# -- Idiotmatic --
def is_prime(number):
        """Return True if number is prime"""
        for candidate in range(2, number):
                if number % candidate == 0:
                        return False
        return number > 0



#Example 15: Prefer absolute imports to relative imports
# -- Harmful --
# Assuming my location is package.sub_package.module
# and I want to import package.other_module
from ...package import other_module # <-- bad

# -- Idiomatic --
import package.other_module 
#or..
import package.other_module as other



#Example 16: Do not use from foo import * to import the contents of a module.
# -- Harmfull --
from foo import *

# -- Idiomatic --
from foo import (bar, baz, qux, quux, quuux)
#or even better..
import foo

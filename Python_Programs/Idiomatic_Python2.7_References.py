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

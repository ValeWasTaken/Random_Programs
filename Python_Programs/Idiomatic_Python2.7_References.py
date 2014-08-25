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

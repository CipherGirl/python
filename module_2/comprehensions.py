# Corey Scheffer - Comprehensions in Python and How they work

nums = [1,2,3,4,5,6,7,8,9,10]

"""
Simple Comprehension
"""
double = [n*2 for n in nums]
square = [n*n for n in nums]

print(double)
print(square)

# Lambda Function (An anonymous function)
squared_lambda = map(lambda n: n*n, nums) # Better to use list comprehension than map lambda

"""
Conditional Comprehension
"""
even_nums = [n for n in nums if n%2 == 0]
print(even_nums)

"""
Nested Comprehention
""" 
# A (letter, number) pair for each letter in 'abcd' and each number in '0123'
result = []
for letter in 'abcd':
    for number in range(4):
        result.append((letter, number))

print(result)

result_list_comprehension = [(letter, number) for letter in 'abcd' for number in range(4)]
print(result_list_comprehension)

"""
Dictionary Comprehenesion
"""
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

print(list(zip(names, heroes)))

dictionary_comprehension = {name: hero for name, hero in zip(names, heroes)}

print(dictionary_comprehension)

dictionary_comprehension_conditional = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}

print(dictionary_comprehension_conditional)

"""
Set Comprehension
"""
numbers = [1,1,2,3,4,5,1,3,4,5,6,6,7,5,8,9,9,6,7]
set_comprehension = { n for n in numbers }
print(set_comprehension)

"""
Generator Expressions
"""
def gen(nums):
    for n in nums:
        yield n*n

my_gen = gen(nums)
gen_expression = (n*n for n in nums)

for i in my_gen:
    print(i)

for i in gen_expression:
    print(i)

print(my_gen, gen_expression)


# Tech with Tim
"""
Comprehension with Multiple Conditions
"""

# String that starts with 'a' and end in 'y'
options = ['any', 'albany', 'apple', 'world', 'hello']
valid_strings = []

for string in options:
    if len(string) <= 1:
        continue

    if string[0] != "a":
        continue

    if string[-1] != "y":
        continue

    valid_strings.append(string)

print(valid_strings)

valid_strings_comprehended = [
    string for string in options
    if len(string) > 1
    if string[0] == 'a'
    if string[-1] == 'y'
]

print(valid_strings_comprehended)

# Flattening a matrix (lists of lists)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)

print(flattened)
# First for loop is the outmost loop and left ones are the nested ones
flattened_comprehension = [num for row in matrix for num in row]

print(flattened_comprehension)

# 3D list
list_3d = []
for a in range(1,4):
    l1 = []
    for b in range(1,4):
        l2 = []
        for c in range(1,4):
            l2.append(c)
        l1.append(l2)
    list_3d.append(l1)

print(list_3d)

list_3d_comprehension = [[[x for x in range(1,4)] for _ in range(1,4)] for _ in range(1,4)]

print(list_3d_comprehension)

"""
Conditional if else comprehension
"""
even_odd = ["Even" if num % 2 == 0 else "Odd" for num in range(11)]
print(even_odd)

"""
Transformation in Comprehension
"""

def square(n):
    return n*n

squared = [square(n) for n in range(4)]
print(squared)

"""
Dictionary Comprehension
"""

pairs = [('a', 1), ('b', 2), ('c', 3)]

dictionary_comprehension_2 = {k: v for k, v in pairs}

print(dictionary_comprehension_2)

"""
Set Comprehensions
"""

squared_set = {n**2 for n in numbers}
print(squared_set)

"""
Generation Comprehension
"""

sum_of_squares = sum(x**2 for x in range(1000000)) # This is the geenrator expression which will yeild the value for every number rather creating all the numbers for the sum function

# sum_of_squares = sum([x**2 for x in range(1000000)]) # This will create the list first and do the sum
print(sum_of_squares)
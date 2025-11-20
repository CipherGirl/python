# Bro Code
# Lambda = A small anonymous function for one time use (throw away function)
#          They take any number of arguments, but have only 1 expression
#          Helps keep the namespace clean and us ysefule with higher order functions
#          sort(), map(), filter(), reduce()
#          lambda parameters: expression

double = lambda x: x*2

print(double(2))

n = [1,2,3,4]

print(list(map(double, n)))

add = lambda x, y: x+y

print(add(1, 2))

max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y

print(max_value(9, 7))

full_name = lambda first, last: first + " " + last

print(full_name("Spongebob", "Squarepants"))

is_even = lambda x: x%2 == 0

is_adult = lambda age: True if age >= 18 else False


# Tech with Tim
numbers = [1,2,3,4,5]

# Map
squares = list(map(lambda x: x**2, numbers))
print(squares)

# Filter
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)

#Sorted
values = [(1, 'b', 'Hello'), (2, 'a', 'World'), (3, 'c', '!')]
sortes_values = list(sorted(values, key=lambda x: x[0]))
print(sortes_values)

# Reduce

from functools import reduce
numbers = [1,2,3,4,5]

# 0 -> acc = 0, num = 1 -> 1
# 1 -> acc = 1, num = 2 -> 3
# 2 -> acc = 3, num = 3 -> 6
# 3 -> acc = 6, num = 4 -> 10
# 4 -> acc = 10, num = 5 -> 15
sum_of_numbers = reduce(lambda acc, num: acc + num, numbers)

print(sum_of_numbers)

numbers = [1,2,3,5,4]

# 0 -> acc = 0, x = 1 -> 1
# 1 -> acc = 1, x = 2 -> 2
# 2 -> acc = 2, x = 3 -> 3
# 3 -> acc = 3, x = 5 -> 5
# 4 -> acc = 5, x = 4 -> 5
max_value_reducer = reduce(lambda acc, x: acc if acc > x else x, numbers)
print(max_value_reducer)

# IIF Lambda
advanced = {x: (lambda x: x**2)(x) for x in range(4)}
print(advanced)
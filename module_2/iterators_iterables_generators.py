# Corey Schafer - Python Tutorial: Iterators and Iterables - What Are They and How Do They Work?
# Iterables have dunder methos __iter__ method
# an iterartor is an object with a state so that it remembers where it is during iteration
# iterators are also iterable
# Iterators cannot go back or change the value
nums = [1, 2, 3]
# i_nums = nums.__iter__()
print(next(iter(nums)))

# for num in nums:
#     print(num)

# i_nums = iter(nums) # nums.__iter__()

# print(i_nums)
# print(divmod)
# print(dir(i_nums))

# # print(next(i_nums))
# # print(next(i_nums))
# # print(next(i_nums))
# # print(next(i_nums))

# # This is below how the for loop does the iteration as well
# while True:
#     try: 
#         item = next(i_nums)
#         # print(item)
#     except StopIteration:
#         break


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

# mr = MyRange(10, 20)

# # print(mr.__next__())

# # Generators:
# # Generators don't need to create a manual iter or next. It uses yield

# # yield in Python is a keyword that turns a regular function into a generator, 
# # allowing the function to pause and resume while producing a sequence of values one at a time.

# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1


# m_r = my_range(20, 30)

# # print(next(m_r))

# # Tech with Tim - Python Generators Explained

# # Iterators - An object that enables a  programmer to traverse a container, particularly lists.
# # Generator (newer) - A routine that can be used to control the iteration behavious of a loop. Very similar to a function that returns an array.

# import sys

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# y = map(lambda i: i*2, x);

# print(sys.getsizeof(y))
# print(sys.getsizeof(list(y)))



# """
# The whole point is that

# we didn't have to store

# the sequence in memory.

# We could generate the

# sequence as we looped

# through it. And that is

# really what an iterator is
# """

# # Generator

# """the way that the
# generator works is when
# the yield keyword is
# hit, it pauses the
# execution of the
# function and returns.
# This value to whatever
# is iterating through
# this generator object."""


# def gen(n):
#     for i in range(n):
#         yield(i)


# for i in gen(3):
#     print(i)
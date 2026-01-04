import sys
import gc
import time

# a = 'Hello World'

# print(sys.getrefcount(a))

# mylist = []
# mylist.append(a)

# print(sys.getrefcount(a))
# print(gc.get_referrers(a))

# print(gc.get_count())


# gc.set_debug(True)


# New Example

#=== Different Methods of Manual GC ===

# gc.set_threshold(20_000, 50, 50)
# gc.disable()

class Link:
    def __init__(self, next_link, value):
        self.next_link = next_link
        self.value = value

    def __repr__(self):
        return self.value
    

l = Link(None, 'Main Link')

my_list = []

start = time.perf_counter()

for i in range(5000000):
    l_temp = Link(l, 'L')
    my_list.append(l_temp)


end = time.perf_counter()

print(f'Time taken {end - start}')

print(gc.get_count())
gc.collect(2)

print(gc.get_count())
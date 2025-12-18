"""
NumPy is faster than standard Python for numerical operations primarily because 
its core is implemented in highly optimized, low-level languages like C and Fortran, 
and it is designed for efficient memory use and vectorized operations

Used for large scale numerical operatrions
"""

import numpy as np

print(np.__version__)

my_list = [1, 2, 3, 4]
my_list = my_list * 2
print(my_list)

array = np.array([1, 2, 3, 4])
array = array * 2
print(array)

multi_dim_array = np.array([['A', 'B', 'C'],
                            ['D', 'E', 'F'],
                            ['G', 'H', 'I']])

print(multi_dim_array.ndim)

print(multi_dim_array[0][1]) # Chain Indexing (Generally)
print(multi_dim_array[0, 1]) # Multi dimensional indexing (Numpy)

ace = multi_dim_array[0, 0] + multi_dim_array[0, 2] + multi_dim_array[1, 1]

print(ace)


#========== SLICING ==========

array_2d = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])

# array[start:end:step]
# print(array_2d[::-2])

# Col/Row Selection
# print(array_2d[:, 1:4])

print(array_2d[0:2, 0:2])
print(array_2d[0:2, 2:])
print(array_2d[2:, 0:2])
print(array_2d[2:, 2:])





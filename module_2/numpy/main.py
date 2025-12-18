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


#========= Scalar ============
# Used for scalar operands (sinlge value)
array_1d = np.array([1.2, 2.4, 3.1])

print(array_1d + 1)
print(array_1d - 2)
print(array_1d * 3)
print(array_1d / 4)
print(array_1d ** 5)

#==== Vectorized Math =====
# Used for applying math functions to the entire array without loop  

print(np.sqrt(array_1d))
print(np.floor(array_1d))
print(np.ceil(array_1d))
print(np.round(array_1d))

# EXERCISE - Area of a circle from radius
radius = np.array([2,3,4])

print(np.pi * radius**2) # pi x r^2

#== Element wise arithmetic ==
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)

#==== Comparison Operators ====
scores = np.array([92, 55, 100, 73, 82, 64])

print(scores > 60)
scores[scores < 60] = 0
print(scores)


#=== SKIPPED BROADCASTING ===

#==== Aggregate Function ==== 
array_aggr = np.array([[1,2,3,4,5],
                       [6,7,8,9,10]])

print(np.sum(array_aggr))
print(np.mean(array_aggr))
print(np.std(array_aggr)) # standard deviation
print(np.var(array_aggr)) # variant - squared of std
print(np.min(array_aggr))
print(np.max(array_aggr))
print(np.argmin(array_aggr)) # index of min value

print(np.sum(array_aggr,axis=0)) # 0 for all columns, 1 for sum all rows
print(np.sum(array_aggr,axis=1)) # 0 for all columns, 1 for sum all rows

#===== Filtering =======
ages = np.array([[21, 16, 14, 20, 18, 65], 
                [39, 22, 15, 99, 21, 20]])

# Creates a new array based on the filter
teens = ages[ages < 18]
adults = ages[(ages > 18) & (ages < 65)]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(teens, adults)

# If need to preserve the shape of data where is preferred
seniors = np.where(ages >= 65, ages, np.nan)

print(seniors)

#==== SKIPPED Random number =====
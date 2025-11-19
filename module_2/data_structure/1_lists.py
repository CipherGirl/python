"""
Ordered, mutable (can change), allows duplicates.

Defined using square brackets [].
"""

fruits = ["apple", "banana", "cherry"]

print(fruits[0])  

fruits[1] = "blueberry"


fruits.append("orange")  
fruits.insert(1, "mango") 

fruits.remove("cherry")
popped = fruits.pop()

for fruit in fruits:
    print(fruit)

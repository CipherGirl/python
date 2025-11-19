"""
Ordered, immutable (cannot change), allows duplicates.

Defined using parentheses ().
"""

colors = ("red", "green", "blue")

print(colors[1])

person = ("Alice", 30)

print(f"{person[0]} is age of {person[1]}")

for color in colors:
    print(color)
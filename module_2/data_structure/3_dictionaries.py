"""
Unordered (Python ≥3.7 preserves insertion order), key-value pairs, mutable.

Keys are unique.
"""

student = {"name": "Alice", "age": 25, "grade": "A"}

print(student["name"]) 

student["age"] = 26
student["city"] = "New York"

student.pop("grade")
del student["city"]

for key, value in student.items():
    print(key, value)

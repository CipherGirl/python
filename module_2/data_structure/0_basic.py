from collections import deque

val1 = 1
val2 = 1

print(id(val1) == id(val1))

cart = []               
cart.append("apple")    
cart.extend(["banana","orange"]) 
print(cart[0])          
cart[1] = "ripe banana" 
cart.pop()              

phone = {"Alice": "+1-555-123", "Bob": "+44-222-999"}
phone["Charlie"] = "+91-987-654"  
print(phone.get("Alice"))         
del phone["Bob"]                  


coord = (10, 20)        
x, y = coord            


visitors = set()
visitors.add("alice")
visitors.add("bob")
"alice" in visitors  


stack = []
stack.append(1)    
stack.append(2)
top = stack.pop()  


q = deque()
q.append("task1")    
q.append("task2")
item = q.popleft()   


student = {"name": "Alice", "age": 25, "grade": "A"}

# print(type(student))

# Python Object VS Dictionary

class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")

print(type(p))
print(type(student))
print(p.name)
print(p.__dict__['name']) 
print(student.__dict__)

# Objects with __slots__ or built-in types (like int, str) don’t use a dict to store attributes
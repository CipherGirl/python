#  Subclasses should be replaceable with their base class without breaking behavior.

"""
Bad Example

from abc import ABC, abstractmethod


class Member(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def save_database(self):
        pass

    @abstractmethod
    def pay(self):
        pass
        

class Student(Member):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def save_database(self):
        print("Saving student data to database")

    def pay(self):
        print("Paying")



class Teacher(Member):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        print("Saving teacher data to database")

    def pay(self):
        raise NotImplementedError("It is free for students!")
"""

from abc import ABC, abstractmethod


class Member(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def save_database(self):
        pass
    

class Subscriber(ABC):
    @abstractmethod
    def pay(self):
        pass
        

class Student(Member, Subscriber):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def save_database(self):
        print("Saving student data to database")

    def pay(self):
        print("Paying")



class Teacher(Member):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        print("Saving teacher data to database")

    def pay(self):
        raise NotImplementedError("It is free for students!")
    

"""💡 Simple Explanation:

“Now every subclass can replace the parent without errors. 
LSP ensures the behavior remains consistent, no surprises for the main system.”
"""
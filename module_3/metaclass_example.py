class MyMeta(type):
    def __new__(cls, name, bases, clsdict):
        clsdict['show'] = lambda self: 'Hello from MyMeta'

        return super().__new__(cls, name, bases, clsdict)
 
class MyClass(metaclass=MyMeta):
    pass

m = MyClass()
print(m.show())
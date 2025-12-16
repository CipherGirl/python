class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def total(self, *args, **kwargs):
        total = 0

        for arg in args:
            if isinstance(arg, (list, tuple)):
                total += sum(arg)
            else:
                total += arg

        total += sum(kwargs.values())
        return total


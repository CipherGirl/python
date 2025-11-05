class Owner:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone


class Dog:
    def __init__(self, name, breed, owner):
         self.name = name
         self.breed = breed
         self.owner = owner


owner1 = Owner("Hasna", "25th Kamal Ataturk Ave", "0123456789")
dog1 = Dog("Snow", "Husky", owner1)

print(dog1.name, dog1.owner.name)


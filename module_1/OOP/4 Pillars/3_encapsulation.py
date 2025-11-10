"""
| Modifier      | Syntax        | Access Level                                         | Meaning                |
| ------------- | ------------- | ---------------------------------------------------- | ---------------------- |
| **Public**    | `self.name`   | Accessible from **anywhere**                         | No underscore          |
| **Protected** | `self._name`  | Should be accessed only **within class or subclass** | Single underscore `_`  |
| **Private**   | `self.__name` | Accessible **only inside the class** (name mangled)  | Double underscore `__` |
"""


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # This is a variable with one underscore meant for internal uses, altough python don't restrict the access but by convenstion we don't access this outside the class.
        self.password = password

        self.__initial_username = username # Name mangling happens which basically changes the name

    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        self._email = new_email

    def get_initial_username(self):
        return self.__initial_username
    
    def get_username(self):
        return self.username
    
    def set_username(self, new_username):
        self.username = new_username

    # Python ways of getter and setter
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, new_email):
        self._email = new_email



user1 = User("hasna_hena_mow", "mow@email.com", "123")

# user1._email = 'hello.com'

user1.set_email("mow@hello.com")
# print(user1.get_email())
print(user1.email)

# print(user1.get_username())
user1.set_username("hena")

print(user1.get_initial_username())
print(user1.get_username())

user1.email = "mow@gmail.com"
print(user1.email)

# print(user1.__initial_username)
print(user1._User__initial_username)




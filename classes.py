class User:
    # Constructor - function that runs when you instantiate an object from a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and i am {self.age} years old'
    
    def has_birthday(self):
        self.age += 1

# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.name} and i am {self.age} years old and my balance is {self.balance}'


# initialise user object
jake = User('Jake Muller', 'jake@gmail.com', 50)

# initialize customer object
jane = Customer('Janet Muller', 'janet2yahoo.com', 35)
jane.set_balance(500)
print(jane.greeting())

jane.greeting()


# print(type(jake))
# print(jake.name)
jake.has_birthday()
print(jake.greeting())

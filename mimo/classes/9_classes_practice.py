# What's wrong with the following code?

class Contact:
    first = "Jane"
    last = "Doe"
    cell = "3112445656"
    email = "jdoe@gmail.com"

jane = Contact()
print(self.email)

# We have to use the jane object, not the self keyword.
# -----------------------------------------------------------------------------
# How many parameters can we add to the constructor method?

# As many as we want.
# -----------------------------------------------------------------------------
# Where does the constructor method go in a class definition?

# It's the first method in the class definition, with the name __init__
# -----------------------------------------------------------------------------
# What is the difference between name and self.name in the following code?

class Person:
    def __init__(self, name):
        self.name = name

anna = Person("Anna")

# name refers to the value passed when the instance is created
# and self.name refers to the class variable, name
# -----------------------------------------------------------------------------
# What's wrong with this code?

class Person:
    def __init__(name, language):
        self.name = name
        self.language = language

# self needs to be the first parameter of the __init__ method
# -----------------------------------------------------------------------------
# Create a constructor method for the Bank_Account class that takes in a name, number, and withdraw.

class Bank_Account:
    def __init__(self, name, number, withdraw):
# -----------------------------------------------------------------------------
# Add the variables name, number and withdraw to the class constructor 
# and set them to be the corresponding parameters.

class Bank_Account:
    def __init__(self, name, number, withdraw):
        self.name = name
        self.number = number
        self.withdraw = withdraw
        self.balance = 1000
# -----------------------------------------------------------------------------
# Update the balance variable to be 1000 minus the class's withdraw's value.

class Bank_Account:
    def __init__(self, name, number, withdraw):
        self.name = name
        self.number = number
        self.withdraw = withdraw
        self.balance = 1000-self.withdraw
# -----------------------------------------------------------------------------
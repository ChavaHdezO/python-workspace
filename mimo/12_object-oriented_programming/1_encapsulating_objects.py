# -----------------------------------------------------------------------------
# Let's learn about different styles of coding used by developers. 
# We'll explore functional programming and object-orientated programming.

# Different styles of coding are also known as paradigms. 
# A common style is called functional programming, or FP for short.

# In functional programming, we use a lot of functions and variables.

def getTotal(a, b):
    return a + b

num1 = 2
num2 = 3
total = getTotal(num1, num2)
print(total)
# -----------------------------------------------------------------------------
# In the FP style, we keep data and functionality separate. 
# We pass data into functions whenever we want something.

def getDistance(mph, h):
    return mph * h

mph = 60
h = 2

distance = getDistance(mph, h)
# -----------------------------------------------------------------------------
# In functional programming, functions return new values 
# and then use those values somewhere else in the code.

def getDistance(mph, h):
    return mph * h

mph = 60
h = 2

distance = getDistance(mph, h)
print(distance)
# -----------------------------------------------------------------------------
# In object-oriented programming (OOP), 
# we group data and functionality as properties and methods inside objects, like Virtual_Pet here.

class Virtual_Pet:
    def __init__(self, color, name):
        self.color = color
        self.name = name

rocky = Virtual_Pet("brown", "rocky")

print(rocky.color)
print(rocky.name)
# -----------------------------------------------------------------------------
# In OOP, we group together related data and functions in the same object. We call this encapsulation.

class Dog:
    name = 'Fido'
    hungry = False

    def eat(self):
        self.hungry = True
# -----------------------------------------------------------------------------
# In FP, code is not encapsulated. Can you explain why this code does not show encapsulation?

# The data and the function are not grouped together in an object.
# -----------------------------------------------------------------------------
# We can spot code that isn't well encapsulated
# if related methods and properties are in different objects.
# How can we encapsulate this code?

class Dog:
    hungry = True

def eat():
    hungry = False

# Move eat() inside the Dog class.
# -----------------------------------------------------------------------------
# In OOP, we identify which methods and properties belong together and should be added to our objects.

class Cat:
    color = 'orange'

    def meow(self):
        print('Meow')

class Car:
    color = "gray"

    def drive(self):
        print("accelerating...")

# -----------------------------------------------------------------------------
# With encapsulation, we also have methods that use the other properties that belong to the object,
# like in this example eat accesses hungry.

class Dog:
    name = 'Fido'
    hungry = True

    def eat(self):
        self.hungry = False

# -----------------------------------------------------------------------------
# What is encapsulation?

# Grouping related data and functions in the same object.
# -----------------------------------------------------------------------------
# Is this code encapsulated?

class Car:
    color = 'red'
    on = False
    def start(self):
        self.on = True

# Yes
# -----------------------------------------------------------------------------
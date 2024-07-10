# -----------------------------------------------------------------------------
# Classes can have functions too, which are known as methods when they're inside of a class.
# Like the bark() method here.

class Virtual_Pet:
    color = "brown"

    def bark(self):
        print("Bark")

rocky = Virtual_Pet()
rocky.bark()
# -----------------------------------------------------------------------------
# self is a special keyword that we need to use inside our class definition.
# We pass self as the first parameter to all the methods we add.

class Virtual_Pet:
    color = "brown"

    def bark(self):
        print("Bark")

rocky = Virtual_Pet()
rocky.bark()
# -----------------------------------------------------------------------------
# We use self as a parameter in the class methods
# so that we can access the class variables like color and legs inside the methods.

class Virtual_Pet:
    color = "brown"
    legs = 4

    def bark(self):
        print("Bark")

    def display_color(self):
        print(self.color)

    def display_legs(self):
        print(self.legs)

rocky = Virtual_Pet()
rocky.display_color()
rocky.display_legs()
# -----------------------------------------------------------------------------
# Inside display_color(), self.color is how we access the value of the class variable color = "brown".

class Virtual_Pet:
    color = "brown"
    legs = 4

    def bark(self):
        print("Bark")

    def display_color(self):
        print(self.color)

    def display_legs(self):
        print(self.legs)

rocky = Virtual_Pet()
rocky.display_color()
rocky.display_legs()
# -----------------------------------------------------------------------------
# To use a class method, it's the same as using a class variable, except we need to add parentheses.
# Like here with rocky.bark().

class Virtual_Pet:
    color = "brown"

    def bark(self):
        print("Bark")

rocky = Virtual_Pet()

print(rocky.color)
rocky.bark()
# -----------------------------------------------------------------------------
# Which is true about a class definition?

# You can create functions and variables in a class definition
# -----------------------------------------------------------------------------
# How do we access rocky's method print_color?

class Dog:
    def __init__(self):
        self.color = "brown"
    def print_color(self):
        print(self.color)

rocky = Dog()

# rocky.print_color()
# -----------------------------------------------------------------------------
# Which of the following is the correct way to access rocky's variable color?

class Dog:
    color = "brown"

    def print_color(self):
        print(self.color)

rocky = Dog()

# rocky.color
# -----------------------------------------------------------------------------
# Why do we need to use the keyword self when accessing class variables from inside a method?

# We need to use self to make class variables scope accessible inside a method
# -----------------------------------------------------------------------------
# Define a class method called introduce inside the class Pokemon.

class Pokemon:
    name = "pikachu"

    def introduce(self):

    print("Hi!")
# -----------------------------------------------------------------------------
# Complete the display statement that display's the name variable by coding self.name.

class Pokemon:
    name = "pikachu"

    def introduce(self):
        print("Hi!")
        print("I am " + self.name)
# -----------------------------------------------------------------------------
# Access and call the method introduce using the class instance pikachu.

class Pokemon:
    name = "pikachu"

    def introduce(self):
        print("Hi!")
        print("I am " + self.name)

pikachu = Pokemon()
pikachu.introduce()
# -----------------------------------------------------------------------------
# Display pikachu's color variable in the console by coding pikachu.color.

class Pokemon:
    name = "pikachu"
    color = "yellow"

    def introduce(self):
        print("Hi!")
        print("I am " + self.name)

pikachu = Pokemon()
pikachu.introduce()
print(pikachu.color)
# -----------------------------------------------------------------------------
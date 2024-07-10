# -----------------------------------------------------------------------------
# There's a method we can use that is more flexible when creating different instances from a class.
# It's called the constructor method.

class Virtual_Pet:
    def __init__(self, color):
        self.color = color

rocky = Virtual_Pet("brown")
benny = Virtual_Pet("black")

print(rocky.color)
print(benny.color)
# -----------------------------------------------------------------------------
# The constructor method looks like __init__()
# and allow us to set unique values for the class variables when we create an instance.

# Make sure to use double underscores on each side of init.

class Virtual_Pet:
    def __init__(self, color):
        self.color = color

rocky = Virtual_Pet("red")
# -----------------------------------------------------------------------------
# Instead of a class definition that will always have the same color,
# a constructor method allow us to specify what we want when creating it.

class Virtual_Pet:
    def __init__(self, color):
        self.color = color

rocky = Virtual_Pet("red")
# -----------------------------------------------------------------------------
# When we create an instance from the class definition,
# we're able to pass unique values inside the parentheses, like with yellow here.

class Virtual_Pet:
    def __init__(self, color):
        self.color = color

rocky = Virtual_Pet("yellow")
# -----------------------------------------------------------------------------
# To add this flexibility to our classes, we start by adding the construction function, 
# which looks like __init__().

class Virtual_Pet:
    def __init__()
# -----------------------------------------------------------------------------
# Just like with regular class methods, 
# we need to add self as the first parameter to the constructor method.

class Virtual_Pet:
    def __init__(self):
# -----------------------------------------------------------------------------
# Next, we add the parameters for the custom values we want to set when we create the instance,
# like with color here.

class Virtual_Pet:
    def __init__(self, color):
# -----------------------------------------------------------------------------
# Then we set the value by coding self, a ., the parameter name, 
# and then equating it to the parameter name again. This sets the value.

class Virtual_Pet:
    def __init__(self, color):
        self.color = color
# -----------------------------------------------------------------------------
# When we create an instance from the class definition, 
# we add the values we want to set inside parentheses, like here with "red".

class Virtual_Pet:
    def __init__(self, color):
        self.color = color

rocky = Virtual_Pet("red")
print(rocky.color)
# -----------------------------------------------------------------------------
# The constructor method helps us construct the instances of our class the way we want.
# We're able to add as many parameters as we want.

class Virtual_Pet:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

rocky = Virtual_Pet("red", 4)
print(rocky.color)
print(rocky.legs)
# -----------------------------------------------------------------------------
# We can access the parameters from other places in the class definition by using self, 
# like self.color here.

class Flower:
    def __init__(self, kind, color):
        self.kind = kind
        self.color = color

    def display_color(self):
        print(self.color)

rose_flower = Flower("rose", "red")
print(rose_flower.kind)
rose_flower.display_color()
# -----------------------------------------------------------------------------
# What is the purpose of a constructor?

# To construct an instance of a class object with unique class variables
# -----------------------------------------------------------------------------
# How do we define the constructor method?

# def __init__(self):
# -----------------------------------------------------------------------------
# When do we use the keyword self?

# When we need to access class variables or methods inside the class definition
# -----------------------------------------------------------------------------
# Can we use parameters when defining the constructor method?

# Yes, we set values for the parameters when creating an instance
# -----------------------------------------------------------------------------
# Add the constructor method to the following class definition.

class Pokemon:
    def __init__(self):
# -----------------------------------------------------------------------------
# Add two parameters to the constructor method, color and name.

class Pokemon:
    def __init__(self, color, name):
# -----------------------------------------------------------------------------
# Set the class variables to be the parameters of the constructor method using the keyword self.

class Pokemon:
    def __init__(self, color, name):
        self.color = color
        self.name = name
# -----------------------------------------------------------------------------
# Using the constructor, 
# create a Pokemon instance that has the color "orange" and the name "charizard".

class Pokemon:
    def __init__(self, color, name):
        self.color = color
        self.name = name

charizard = Pokemon("orange", "charizard")

print(charizard.color)
print(charizard.name)
# -----------------------------------------------------------------------------
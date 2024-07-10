# -----------------------------------------------------------------------------
# As we build programs, we'll often need to create many similar but distinct objects.
# Like various different configurations of a computer.

computer1_size = "15"
computer1_storage = "1TB"

computer2_size = "13"
computer2_storage = "256GB"

print("computer1 display size: " + computer1_size)
print("computer1 storage space: " + computer1_storage)

print("computer2 display size: " + computer2_size)
print("computer2 storage space: " + computer2_storage)
# -----------------------------------------------------------------------------
# Creating new variables for each of the different configurations of a computer would take a lot of time
# and could lead to mistakes.

computer1_size = "15"
computer1_storage = "1TB"

computer2_size = "13"
computer2_storage = "256GB"

computer3_size = "27"
computer3_storage = "2TB"

computer4_size = "21"
computer4_storage = "512GB"

computer5_size = "11"
computer4_storage = "128"
# -----------------------------------------------------------------------------
# To help us group data and functionality, we create a class.
# A class is a template that we use to create many similar but distinct things.

class Computer:
    def __init__(self, size, storage):
        self.size = size
        self.storage = storage

    def print_specs(self):
        print("Display size: " + self.size)
        print("Storage size: " + self.storage)

low_spec = Computer("13", "256GB")
high_spec = Computer("27", "1TB")

print("Low Spec Computer:")
low_spec.print_specs()

print("High Spec Computer:")
high_spec.print_specs()
# -----------------------------------------------------------------------------
# By using a template, we can create different configurations without having to create individual
# variables like size and storage each time.

class Computer:
    def __init__(self, size, storage):
        self.size = size
        self.storage = storage
        
    def print_specs(self):
        print("Display size: " + self.size)
        print("Storage size: " + self.storage)
        
low_spec = Computer("13", "256GB")
mid_spec = Computer("15", "512GB")
high_spec = Computer("17", "1TB")
premium_spec = Computer("17", "2TB")
# -----------------------------------------------------------------------------
# To start creating the template we add the keyword class followed by a name and a colon.
# Here, we'll create the class, called Person:

class Person:
# -----------------------------------------------------------------------------
# To add code to the class, we indent from the keyword class.
# Like with the print() statement here.

class Person:
    print("inside the class")
# -----------------------------------------------------------------------------
# Creating a variable inside a class works just like creating normal variables.
# It needs to be properly indented and assigned a value.

class Person:
    nationality = "French"
# -----------------------------------------------------------------------------
# We can add as many variables as we'd like inside a class,
# like with variable hobby with the value "Cooking" here.

class Person:
    nationality = "French"
    hobby = "Cooking"
# -----------------------------------------------------------------------------
# Should the following code be group into a class?
person1_name = "Jess"
person1_age = 24

person2_name = "Tom"
person2_age = 77

person3_name = "Emily"
person3_age = 5

# Yes, a class could group a person with the variable's 'name' and 'age'
# -----------------------------------------------------------------------------
# Which of the following is the correct way to define a class using the keyword class?
class Grocery:
# -----------------------------------------------------------------------------
# Which scenario does it make sense to use a class instead of multiple variables?
# Coding an online store where there are items with a picture and name
# -----------------------------------------------------------------------------
# How many variables can we add to a class?
# As many as we want
# -----------------------------------------------------------------------------
# Assemble a class using the keyword class, the class name Flower, and :
class Flower:
    color = 'red'
# -----------------------------------------------------------------------------
# Add a print statement in the class that prints the variable 'color'.
class Flower:
    color = 'red'
    print(color)
# -----------------------------------------------------------------------------
# Add another variable to the class called species and set the value to be rose.
class Flower:
    color = "red"
    print(color)
    species = "rose"
# -----------------------------------------------------------------------------
# Assemble a Bird class and define a variable called 'can_fly' that has the value True.
class Bird:
    can_fly = True
# -----------------------------------------------------------------------------
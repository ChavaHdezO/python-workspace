# As a volunteer at a festival, you track the rides being installed.
# We have a class named Ride that stores the name of the ride and the suitable age group.
# Use instances of that class to track the rides installed today.

# 1. Create a new instance of the Ride class named roller_coaster 
# and specify that its name is Roller coaster and an adults ride.
# 2. Create a new instance of the Ride class named ferris_wheel 
# and specify that its name is Ferris wheel and a kids ride.

class Ride:
    def __init__(self, name, age_group):
        self.name = name
        self.age_group = age_group

roller_coaster = Ride("Roller coaster", "adults")
ferris_wheel = Ride("Ferris wheel", "kids")
print(roller_coaster.age_group)
print(ferris_wheel.name)
# -----------------------------------------------------------------------------
# There's a cafe nearby that offers a new variety of beverages every day.
# We have a Beverage class and two instances: fruity and cocoa.
# Find out what's in today's drinks.

# 1. Access the name property of the fruity beverage and print it to the console.
# 2. Access the is_alcoholic property of the cocoa beverage and print it to the console.

class Beverage:
    def __init__(self, name, is_alcoholic):
        self.name = name
        self.is_alcoholic = is_alcoholic

fruity = Beverage("Fruit punch", False)
cocoa = Beverage("Hot chocolate", False)
print(fruity.name)
print(cocoa.is_alcoholic)
# -----------------------------------------------------------------------------
# You're a pet lover and have different pets at home.
# Your sibling is visiting you and they can't remember the names of your pets.
# Finish the Pet class to help your sibling associate a pet's name with its properties, 
# like its family or color.

# 1. Within the Pet class, create instance variables name, 
# family, animal_type and color to store the specific information received in the parameters.

class Pet:
    def __init__(self, name, family, animal_type, color):
        self.name = name
        self.family = family
        self.animal_type = animal_type
        self.color = color

rio = Pet("Rio", "Macaw", "Parrot", "Blue")
coco = Pet("Coco", "Poodle", "Dog", "White")
bud = Pet("Bud", "Labrador", "Dog", "Brown")
daisy = Pet("Daisy", "Burmese", "Cat", "Grey")
print(f"{rio.name} is a {rio.color} colored {rio.family} {rio.animal_type}")
# -----------------------------------------------------------------------------
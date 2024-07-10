# -----------------------------------------------------------------------------
# When we want to use our class template to create something, we start by creating a variable,
# like fluffy here.

class VirtualPet:
    color = "brown"

fluffy = 
# -----------------------------------------------------------------------------
# Next, we add the class name and parentheses to create it, like with Virtual_Pet() here.

class VirtualPet:
    color = "brown"

fluffy = VirtualPet()
# -----------------------------------------------------------------------------
# When we create variables from the class template, we're creating instances.
# fluffy and benny are instances of the VirtualPet class.

class VirtualPet:
    color = "brown"

fluffy = VirtualPet()
benny =  VirtualPet()
# -----------------------------------------------------------------------------
# The VirtualPet class we're using to create the fluffy variables is called the definition.
# VirtualPet is the definition, fluffy is an instance.

class VirtualPet:
    color = "brown"
    legs = 4
    lives = "9"

fluffy = VirtualPet()
# -----------------------------------------------------------------------------
# To access a class variable, we add the instance name, a ., and the name of the variable we want.
# Like skippy.wagging_tail here.

class VirtualPet:
    wagging_tail = True
    color = "brown"

skippy = VirtualPet()
print(skippy.wagging_tail)
# -----------------------------------------------------------------------------
# We can access all of the variables we created in the class definition.
# We access the value of the variable color by coding skippy.color.

class VirtualPet:
    wagging_tail = True
    color = "brown"

skippy = VirtualPet()
print(skippy.wagging_tail)
print(skippy.color)
# -----------------------------------------------------------------------------
# Which piece of code correctly creates an instance of a class called Cat?

fluffy = Cat()
# -----------------------------------------------------------------------------
# What does this code do?

class VirtualPet:
    color = "brown"

fluffy = VirtualPet()

# We're defining a class and creating an instance of it
# -----------------------------------------------------------------------------
# What's happening in this code?

class VirtualPet:
    wagging_tail = True

# We're defining a class
# -----------------------------------------------------------------------------
# What's the correct way to access an instance's variable?

# instance.variable
# -----------------------------------------------------------------------------
# Inside the print() statement, display the variable wagging_tail of the spot instance.

class VirtualPet:
    wagging_tail = True

spot = VirtualPet()
print(spot.wagging_tail)
# -----------------------------------------------------------------------------
# Create an instance if the Pokemon class and store it in a variable called pokemon.

class Pokemon:
    name = "squirtle"

pokemon = Pokemon()

print(pokemon.name)
# -----------------------------------------------------------------------------
# Display the color of the class instance rocky.

class VirtualPet:
    color = "brown"

rocky = VirtualPet()
print(rocky.color)
# -----------------------------------------------------------------------------
# Add a variable called weight to the class definition and set "19.8" as its value.

class Pokemon:
    name = "squirtle"
    weight = "19.8"

pokemon = Pokemon()
print(pokemon.name)
print(pokemon.weight)
# -----------------------------------------------------------------------------
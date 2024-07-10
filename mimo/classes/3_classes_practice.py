# -----------------------------------------------------------------------------
# Add a class variable called retailers that contains a list of strings of stores
# where you can buy the camera.

class Camera:
    value = "$800"
    model = "Canon EOS M6"
    retailers = ["Walmart", "eBay", "Amazon"]
# -----------------------------------------------------------------------------
# What is class?

# A template that can have variables and functionality associated with it
# -----------------------------------------------------------------------------
# How do we create a class definition?

# Using the keyword class followed by the name and a colon
# -----------------------------------------------------------------------------
# What's wrong with this code?

class :

# The class is missing a name
# -----------------------------------------------------------------------------
# What are variables inside a class used for?

# To store data that is related to the given class
# -----------------------------------------------------------------------------
# Can we use the keyword class to create a class object instance?

# No, we need the class name followed by ()
# -----------------------------------------------------------------------------
# Why do we need to store the class instance in a variable?

# So we can access the class instance
# -----------------------------------------------------------------------------
# Create an instance of the class Virtual_Pet and store it in a variable callec cat.

class Virtual_Pet:
    name = "Whiskers"

cat = Virtual_Pet()
# -----------------------------------------------------------------------------
# Add the variable breed to the class and assign it the string "tabby".

class Virtual_Pet:
    name = "Whiskers"
    breed = "tabby"

cat = Virtual_Pet()
# -----------------------------------------------------------------------------
# Display the name variable from the class instance, cat, using a print statement.

class Virtual_Pet:
    name = "Whiskers"
    breed = "tabby"
    is_trained = True

cat = Virtual_Pet()
print(cat.name)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Create a class called Player and print its variable level inside the definition.

class Player:

    level = 1
    print(level)
# -----------------------------------------------------------------------------
# Add a print statement that is inside the class definition, displaying the variable show.

class TV_Show:
    show = "Spongeob Circleshirt"
    channel = "Nickelodeon"
    print(show)
# -----------------------------------------------------------------------------
# Add a variable called channel_num to the class and set its value to 56.

class TV_Show:
    show = "Spongebob Circleshirt"
    channel = "Nickelodeon"
    print(show)
    channel_num = 56
# -----------------------------------------------------------------------------
# What is necessary when defining a class?

# Making sure the code in the definition is indented
# -----------------------------------------------------------------------------
# How many variables does this class have?

class Pet:
    name = "Sparky"
    breed = "Labrador"
    age = 6

color = "white"

# 3
# -----------------------------------------------------------------------------
# What happens when we un-indent the print statement in the class definition?

class Virtual_Pet:
    print("inside the class definition")

# We'll get an error
# -----------------------------------------------------------------------------
# What are classes used for?

# To reduce repeated code by grouping it into a class
# -----------------------------------------------------------------------------
# What's wrong with this code?

class Musical:
    name = "Hamilton"
    length = "2h 40m"
songs = 46

hamilton = Musical()
print(hamilton.songs)

# The variable songs should be indented to be a part of the class definition
# -----------------------------------------------------------------------------
# How many variables does the class instance wicked have?

class Musical:
    name = "Wicked"
    length = "2h 30m"
    songs = 19

wicked = Musical()

# 3
# -----------------------------------------------------------------------------
# What's wrong with this code?

class Musical:
    name = "Hamilton"
    length = "2h 40m"
    songs = 46

print(hamilton.name)

# We haven't created an instance of the class so there doesn't exist a name variable
# -----------------------------------------------------------------------------
# Which of the following is the correct way to create a class instance?

# variable = My_Class()
# -----------------------------------------------------------------------------
# Create a class called Book_Series.

class Book_Series:
    name = "The Hunger Games"
    length = 3

# -----------------------------------------------------------------------------
# Access the length variable of the class instance, hunger_games.

class Book_Series:
    name = "The Hunger Games"
    length = 3

hunger_games = Book_Series()
print(hunger_games.length)
# -----------------------------------------------------------------------------
# Create a variable called countries
# and let it equal a list of the following countries: USA, England and Russia.

class Olympic_Sports:
    name = "Gymnastics"
    countries = ["USA", "England", "Russia"]
# -----------------------------------------------------------------------------
# Write a print statement that displays the first item of the variable countries.

class Olympic_Sports:
    name = "Gymnastics"
    countries = ["USA", "England", "Russia"]

gymnastics = Olympic_Sports()
print(gymnastics.countries[0])
# -----------------------------------------------------------------------------
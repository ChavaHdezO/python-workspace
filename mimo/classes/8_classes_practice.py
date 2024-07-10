# How many methods can we have in a class?

# As many as we want
# -----------------------------------------------------------------------------
# How do we add a method to a class definition?

# We indented it inside the class definition
# -----------------------------------------------------------------------------
# Add a print statement to the call method that print the class's first and last variables.

class Contact:
    first = "Jane"
    last = "Doe"
    cell = "3112445656"
    email = "jdoe@gmail.com"

    def get_call(self):
        print(self.cell)

    def call(self):
        print("calling...")
        print(self.first, self.last)
# -----------------------------------------------------------------------------
# Add a method called call to the class.

class Contact:
    first = "Jane"
    last = "Doe"
    cell = "3112445656"
    email = "jdoe@gmail.com"

    def get_cell(self):
        print(self.cell)

    def call(self):
        print("calling...")
# -----------------------------------------------------------------------------
# What is wrong with the following code?

class Contact:
    first = "Jane"
    last = "Doe"
    cell = "3112445656"
    email = "jdoe@gmail.com"

def get_cell(self):
    print(self.cell)

# The method get_cell needs to be indented
# -----------------------------------------------------------------------------
# How can we assign class variables a value when the class instance is being constructed?

# By adding them as a parameter in the init function 
# and setting the variable equal to the parameter value
# -----------------------------------------------------------------------------
# Create a constructor for the class Song that takes in a name and an artist.

class Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
# -----------------------------------------------------------------------------
# Add a line to the constructor that sets the variable is_playing to be False.

class Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.is_playing = False
# -----------------------------------------------------------------------------
# Create an instance of the class with the name = "Happy Birthday" and the artist = "unknown".

class Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.is_playing = False

song = Song("Happy Birthday", "unknown")
# -----------------------------------------------------------------------------
# Create another instance and store it in the variable next_song. 
# Use the parameters "Happy" and "Pharrell".
class Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.is_playing = False

song = Song("Happy Birthday", "unknown")
next_song = Song("Happy", "Pharrell")
# -----------------------------------------------------------------------------
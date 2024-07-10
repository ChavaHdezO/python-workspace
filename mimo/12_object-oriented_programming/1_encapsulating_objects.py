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
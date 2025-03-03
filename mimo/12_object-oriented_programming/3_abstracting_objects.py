# -----------------------------------------------------------------------------
# Let's use OOP to model a complicated object, like a car. When we drive a car,
# we don't need to understand its inner mechanics.

# Similarly, when working with code, we want to understand the core methods
# without being bogged down by details.

# -----------------------------------------------------------------------------
# A car does a lot of things at the same time. For example, a car injects and
# ignites fuel thousands of times a minute just to stay running.

class Car:
    def injectFuel(self):
        print("Spraying fuel")
    
    def igniteFuel(self):
        print("Boom!")

# -----------------------------------------------------------------------------
# Modeling a car in Python works the same. However, repeatedly calling methods
# can make it harder to read and use.

class Car:
    def injectFuel(self):
        print("Spraying fuel")
    
    def igniteFuel(self):
        print("Boom!")

car = Car()
car.injectFuel()
car.igniteFuel()
car.injectFuel()
car.igniteFuel()

# -----------------------------------------------------------------------------
# Besides that, managing each individual method call by ourselves increases the
# chance we'll make a mistake and cause unwanted effects.

class Car:
    def injectFuel(self):
        print('Spraying fuel')
    
    def igniteFuel(self):
        print('Boom!')

car = Car()
car.injectFuel()
car.injectFuel()
car.igniteFuel()

# -----------------------------------------------------------------------------
# Cars do all of this low-level functionality for us, and we only have to start
# them up. Hiding these details is called abstraction.

class Car:
    def __init__(self):
        self.on = False
    
    def injectFuel(self):
        print('Spraying fuel')
    
    def igniteFuel(self):
        print('Boom!')
    
    def startUp(self):
        self.on = True
        while self.on:
            self.injectFuel()
            self.igniteFuel()

# -----------------------------------------------------------------------------
# We implement abstraction in OOP by writing a few core functions that handle
# all of the low-level work.

class Car:
    def __init__(self):
        self.on = False
    
    def injectFuel(self):
        print('Spraying fuel')
    
    def igniteFuel(self):
        print('Boom!')
    
    def startUp(self):
        self.on = True
        while self.on:
            self.injectFuel()
            self.igniteFuel()

# -----------------------------------------------------------------------------
# Abstraction allows other developers to use a class without having to know
# what low-level methods it has or how they even work.

car = Car()

# -----------------------------------------------------------------------------
# Other developers can create a new object from our Car class and use it by
# just calling a few core methods.

car = Car()
car.startUp()

# -----------------------------------------------------------------------------
# What is abstraction?

# Simplifying how we interact with objects down to a few methods

# -----------------------------------------------------------------------------
# How do we implement abstraction?

# Write a few core methods that handle low-level functions

# -----------------------------------------------------------------------------
# Why is implementing abstraction important?

# So others can use a class without knowing how it works

# -----------------------------------------------------------------------------
# What is one of the benefits of abstraction?

# Fewer bugs caused by user error

# -----------------------------------------------------------------------------
# Which of these could be a core method for a camera?

take_photo()

# -----------------------------------------------------------------------------
# Abstract this class by creating a makeCoffee() method that heats water,
# adds it to coffee grounds, and filters off the coffee.

class Coffeemaker:
    def heatWater(self):
        print('Heating water')
    
    def brew(self):
        print('Adding water to grounds')
    
    def filterCoffee(self):
        print('Filtering coffee')
    
    def makeCoffee(self):
        self.heatWater()
        self.brew()
        self.filterCoffee()

# -----------------------------------------------------------------------------
# To make ice cream, we must both churn and freeze cream. Call the method of 
# iceCreamMaker that does both for us.

class IceCreamMaker:
    def churn(self):
        print('Churning cream')
    
    def freeze(self):
        print('Freezing cream')
    
    def makeIceCream(self):
        self.churn()
        self.freeze()

iceCreamMaker = IceCreamMaker()
iceCreamMaker.makeIceCream()

# -----------------------------------------------------------------------------
# Code translateLive() so that travelers can instantly translate what they say
# into text the locals can read.

class Translator:
    def record(self):
        print('Recording audio')
    
    def transcribeRecording(self):
        print('Converting audio to text')
    
    def translateText(self):
        print('Translating text')
    
    def translateLive(self):
        self.record()
        self.transcribeRecording()
        self.translateText()

# -----------------------------------------------------------------------------
# Call the correct core method that handles the low-level functionality of
# changing slides after displaying each one.

class Slideshow:
    def __init__(self, slides):
        self.slides = slides
        self.current = 1
    
    def viewNextSlide(self):
        self.current += 1
    
    def play(self):
        while self.current <= self.slides:
            print('Slide', self.current)
            self.viewNextSlide()

slideshow = Slideshow(5)
slideshow.play()

# -----------------------------------------------------------------------------
# Choose the correct core method to use from the camera object.

camera = Camera()
camera.takePhoto()
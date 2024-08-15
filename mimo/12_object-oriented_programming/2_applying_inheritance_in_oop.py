# -----------------------------------------------------------------------------
# As we've previously learned, OOP means we encapsulate related data and functions inside objects.
class Person:
    name = "Sam"
    def greet(self):
        print("Hi!")
p = Person()
p.greet()
# -----------------------------------------------------------------------------
# When we create objects one by one we run into the problem of having duplicate code.
# How many greet() methods are there?
class Person1:
    name = "Sam"
    def greet(self):
        print("Hi!")
class Person2:
    name = "Mike"
    def greet(self):
        print("Hi!")
class Person3:
    name = "Jane"
    def greet(self):
        print("Hi!")
# 3
# -----------------------------------------------------------------------------
# We use inheritance to make our code efficient.
# Through inheritance, classes receive methods from other classes.
# -----------------------------------------------------------------------------
# Inheritance lets us create classes that have different properties and behaviors 
# without coding each one from scratch.
class Parent:
    def __init__(self):
        self.eyes = "green"
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.age = 7
child = Child()
print(child.eyes)
print(child.age)
# -----------------------------------------------------------------------------
# Here we see that the Child class is inheriting the Parent class 
# because it's inside the parentheses after the class name.
class Parent:
    def __init__(self):
        self.eyes = "green"
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.age = 7
child = Child()
print(child.eyes)
print(child.age)
# -----------------------------------------------------------------------------
# Let's look at how a class can inherit methods from another.
# When defining the class we add parentheses with the class that we're inheriting.
class Greetings:
    def greet(self):
        print("Hi!")
class Person(Greetings):
    name = "George"
# -----------------------------------------------------------------------------
# The Person class can now use the Greeting's method like its own. 
# Try calling greet() as a method of person.
class Greetings:
    def greet(self):
        print("Hi!")
class Person(Greetings):
    name = "George"
p = Person()
p.greet()
# -----------------------------------------------------------------------------
# We can update how classes work by setting methods directly in the class.
# Define the charge method inside the Hybrid class.
class Car:
    def start_car(self):
        print("Starting car")
class Hybrid(Car):
    def charge(self):
        print("Using fuel to charge battery")
prius = Hybrid()
prius.start_car()
prius.charge()
# -----------------------------------------------------------------------------
# We've learned how flexible Python can be using inheritance.
# Next, we'll dive further into how classes inherit things.
class Car:
    def start_car(self):
        print("Starting car")
class Hybrid(Car):
    def charge(self):
        print("Using fuel to charge battery")
class Electric(Car):
    def fuel(self):
        print("No fuel necessary")
prius = Hybrid()
electric = Electric()
prius.start_car()
electric.start_car()
prius.charge()
electric.fuel()
# -----------------------------------------------------------------------------
# Classes contain a method called a constructor 
# that sets the properties of new objects, known as instances.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

sam = Person("Sam", 23)
print(sam.name, sam.age)
# -----------------------------------------------------------------------------
# We can use the concept of inheritance to reuse parts of code in our classes,
# making our code more readable and efficient.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hi!")

class Nurse(Person):
    def __init__(self, name, age):
        super().__init__("Nurse " + name, age)
    def intro(self):
        print("Hi, I'm", self.name)

person1 = Nurse("Sam", 23)
person2 = Person("Tom", 30)

person1.intro()
person2.greet()
# -----------------------------------------------------------------------------
# When working with classes, we have to think a bit about how to apply inheritance.
# Suppose we wanted to model a student class in our code.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi!")
class Student:
# -----------------------------------------------------------------------------
# We want Student to function like Person, except have a major.
# If we create a new Student class, we end up repeating the code from Person.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hi!")

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def greet(self):
        print("Hi!")
# -----------------------------------------------------------------------------
# Instead, it makes more sense in this case to create a subclass
# that inherits Person's greet() method by coding (Person) after Student.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi!")

class Student(Person):
# -----------------------------------------------------------------------------

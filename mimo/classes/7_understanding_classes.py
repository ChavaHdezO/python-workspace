# Similar to naming variables and functions, there are some common practices when defining classes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

teacher = Person("Emily", 24)
# -----------------------------------------------------------------------------
# Class names usually have the first letter capitalized and the rest lowercase, like with Person here.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# -----------------------------------------------------------------------------
# Like variables, we try to name classes descriptively.

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
# -----------------------------------------------------------------------------
# As with naming variables and functions, 
# we should name things consistently and watch out for capitalization.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello")

    def sayBye(self):
        print("Bye")

teacher = Person("Emily", 24)
teacher.sayBye()
# -----------------------------------------------------------------------------
# Like methods outside of classes, you can use Python's built-in functions and core features.

class Pie:
    def __init__(self, flavor, ingredients):
        self.flavor = flavor
        self.ingredients = ingredients

    def print_ingredients(self):
        for i in self.ingredients:
            print(i)

applePie = Pie('apple', ['flour', 'eggs', 'apples', 'butter'])

applePie.print_ingredients()
# -----------------------------------------------------------------------------
# What's wrong with this code?

Person():
  def __init__(self, age, height):
    self.age = age
    self.height = height

jess = Person(29, 5)
print(jess.age)

# The class keyword is missing
# -----------------------------------------------------------------------------
# How many values can we call the Person constructor with, 
# without changing the given class?

class Person:
    def __init__(self, age, height):
        self.age = age
        self.height = height

jess = Person(29, 5)
print(jess.age)
# -----------------------------------------------------------------------------
# What Python core language features can we use inside a class?

# All of Python's core language features
# -----------------------------------------------------------------------------
# Which of these is not a good naming practice for classes?

# Naming your classes with reserved language keywords like if
# -----------------------------------------------------------------------------
# Create a class that represents different book series, 
# for example, Harry Potter, The Hunger Games, etc.

class BookSeries:
    def __init__(self, name, books):
        self.name = name
        self.books = books
# -----------------------------------------------------------------------------
# Create a method that displays the series name.

class BookSeries:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def print_name(self):
        print(self.name)
# -----------------------------------------------------------------------------
# Create another method that prints the books in the series.

class BookSeries:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def print_name(self):
        print(self.name)

    def print_books(self):
        print(self.books)

hg = BookSeries("Hunger Games", ["The Hunger Games", "Catching Fire", "Mockingjay"])
hg.print_books()
# -----------------------------------------------------------------------------
# Code len(books) to store the length of the list in a variable.

class BookSeries:
    def __init__(self, name, books):
        self.name = name
        self.books = books
        self.num_books = len(books)

    def print_name(self):
        print(self.name)

    def print_books(self):
        print(self.books)

hg = BookSeries("Hunger Games", ["The Hunger Games", "Catching Fire", "Mockingjay"])

hg.print_books()
print(hg.num_books)
# -----------------------------------------------------------------------------

"""
cats = ["whiskers", "tom"] # Index of list start in 0
cats.append("jack") # Add a value at the end of the list
cats.pop() # Removes the last value from a list
cats.insert(1, "willy") # Inserts a value inside a list at the indicated index
for cat in cats: # Loop through the elements of a list
    len(cats) # Get the number of elements inside a list
    print(cats[1]) # Print the element of the indicated index in the list
"""
# When we want to be able to modify the returned collection of values, like updating a team member, we return a list like a team
def form_team(players):
    team=[]
    team.append(players[0])
    team.append(players[2])
    return team

players = ["Sue", "Ed", "Ann", "Ty"]
team = form_team(players)
team[0]="Chloe"
print(team)

# List Comprehensions - Using List Comprehensions
prices = [10, 38, 40, 58, 62] # A list
halved = [] # An empty list
for price in prices: # A loop to iterate through each value inside the list
    half_price = price/2 # A operation
    halved.append(half_price) # Adding the value stored in the half_price variable

halved_lc = [price/2 for price in prices] # We can generate the same list as before, but in one line using list comprehension
# List comprehension is a way to create a new list by applying an expression on each element of an existing list

# List Comprehensions - Functions as Expressions
"""
prices = [10, 22, 30, 40, 58, 62] # A list
def halve(num): # A function
    no_tax = 0.85 * num # We can apply more than one operation using a function
    return no_tax / 2 # The returned value is mandatory

halved = [halve(price) for price in prices] # A list comprehension using a function as a expression
print(halved) # Printing the new list generated
"""
authors = ["Virginia Woolf", "John Steinbeck"] # A list

def add_comma(name): # A function
    parts = name.split(" ") # A variable splitted by " "
    return parts[1] + ", " + parts[0] # A instruction returning a unified string

authors_update = [add_comma(name) for name in authors] # A list comprehension using a function

print(authors_update) # Printing the result

# List Comprehensions - Filtering with If Statements
scores = [12, 47, 30, 29, 19, 35] # A list of numbers
high_scores = [score for score in scores if score > 20] # Creating a list of an existing one, by filtering with a condition
print(high_scores) # Printing the list generated

# List Comprehensions - Negative Indexing and Deletion
scores = [4.5, 5, 3, 4, 3.5, 4] # We can use negative indexing to refer to a value from the end of an indexable object, like a list, by using any negative value up to and including the length of the list
latest = scores[-1]
print(latest)
scores[-3] = 6 # We can also modify list items in the given position
scores[-7] = 8 # We will get an error if we attempt to retrieve a value in a position outside the object's range
# Tuples are also ordered data structures and values can be retrieved, but they are immutable and so cannot be modified.
del scores[-2] # This instruction allow us to delete objects or items within a data structure
del scores # We can use this instruction to delete objects like list, sets, dictionaries too
# We can use del with a key inside a dictionary to remove unwanted key:value pairs from the dictionary
product = {'category': 'book',
           'price': 4.99,
           'in_shop': True}

del product['in_shop']

# List Comprehensions - Slice Notations
# [start:stop:step] # We can use a format with two colons, if we don't put start and stop index value, by default, this will work from the start to the end of the full original list. Each index value can be positive, negative or omitted
ingredients = ["tomato", "cheese", "pepperoni", "bread"] # We can use slicing to retrieve multiple values from a list, we can use negative values too
print(ingredients[0:2]) # Here we get 'tomato' and 'cheese'
print(ingredients[5:]) # If you specify a value out of the range of a list to the start index, we obtain an empty list, rather than an error
print(ingredients[1:2]) # The value in the stop position in a slicing is not included in the obtained list
print(ingredients[:2]) # But if we use a 0 as the start position value, the end position value will be equal to the number of the elements returned
print(ingredients[3:0]) # A start index value that is greater than the stop index value, give us an empty list, rather than an error

# The value to the left of the colon : is the start position for the slice. As we've covered previously, Python indexing starts at zero.
letters = ["A", "B", "C", "D", "E"]
print(letters[4:])
print(letters[1:])

# We can also use a format with two colons, [start:stop:step], where step determines how Python steps between start and end.
alphabet = ["A", "B", "C", "D", "E", "F"]
print(alphabet[1:6:2])

# List Comprehensions 2 - Practicing
#
side = "salad"
meal = ["Steak", "Chips", side]
del meal[-1]
print(side)
#
shopping = ["bananas", "oranges", "lemons", "carrots", "beans"]
if len(shopping) > 3:
    del shopping[-1]

print(shopping)
#
cookies = ["site_access", "adverts"]
permissions = (True, False, False)

if permissions[-1] == False:
    del cookies
    print("Cookies deleted")
#
users = {"Dave": (27, "Manager"),
         "Alexis": (33, "CEO"),
         "Jason": (22, "Apprentice")}

del users["Jason"]
print(users)
#
scrambled = ["X", "y", "3", "o", "e", "l", "5", "l", "a", "e", "f", "H", "z"]

hello = scrambled[-2:2:-2]
print(hello)
#
temperatures = [14, 16, 17, 12, 11]
print(temperatures[-5:])
#
alphabet = ["A", "B", "C"]
selection = alphabet[-2:-1:1]
print(selection)
#
words = ["I", "do", "hate", "not", "love", "you"]

print(words[1::-1])
print(words[-2::])
#
ratings = [4.3, 3.1, 5, 1.1]

recommended = [True if rating > 4 else False for rating in ratings]

print(recommended)
#
websites = ["mimo.com", "coding.com", "food.org"]

def add_https(site):
    return "https://" + site

auto_add = [add_https(site) for site in websites]
print(auto_add)
#
product = {
    'name': 'pencil',
    'type': 'stationery',
    'price': 1.99,
    'color': 'blue',
    'availability': False
}
del product['color']
print(product)

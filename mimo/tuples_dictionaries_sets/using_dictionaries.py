# We need dictionaries to associate each value of a collection with a meaningful "label", instead of an index
"""
# Using Dictionaries - Accesing and Updating Values
actor_bio = { # A dictionary
 "name": "Bill Murray",
 "known for": ["Lost in Translation", "Rushmore"]
}

actor_name = actor_bio["name"]
print(actor_name) # Printing the value of the stored selected key
"""
"""
player_scores = {
 "ann": 13,
 "michael": 20,
 "ava": 34
}

for player in player_scores:
  print(player_scores[player])
"""
"""
ticket = { # A dictionary with two key-value pairs
 "seat no.": 25,
 "first class": False
}

ticket["window"] = True # Adding a key-value pair to the dictionary
ticket["first class"] = True
print(ticket)
"""
"""
winner_scores = {
  "first": ("Ted", 50),
  "second": ("Jess", 47)
}

#for winner in winner_scores:
#  print(winner_scores[winner])
winner_scores.pop("second")
print(winner_scores)
"""
"""
participants = {
  "Meg": True,
  "Kim": False,
}

participants["Kim"] = True
"""
"""
air = {
  "nitrogen": "78%",
  "oxygen": "21%",
  "argon": "0.93%",
  "carbon dioxide": "0.04%", 
  "other": "0.03%"
}

print(air["argon"])
"""
"""
air = {
  "nitrogen": "78%",
  "oxygen": "21%",
  "argon": "0.93%",
  "carbon dioxide": "0.04%", 
  "other": "0.03%"
}

print(air["oxygen"])
"""

participants = {
  "Meg": True,
  "Kim": False,
  "Luis": True,
  "Luis M.": False
}
"""
#meg = participants["Meg"]
kim = participants.pop("Kim")
print(kim)
"""
"""
# Adding a key-value pair
contents = { # A dictionary with three key-value pairs
  "ch. 1": "A long-expected party",
  "ch. 2": "The shadow of the past",
  "ch. 3": "Three is company"
}

contents["ch. 4"] = "A short cut to mushrooms" # Adding a key-value pair to the dictionary

for chapter in contents:
  print(contents[chapter])
"""
"""
toppings = {
  "olives": True,
  "anchovies": False,
  "extra cheese": False
}

toppings["extra cheese"] = True
"""
"""
toppings = {
  "olives": True,
  "anchovies": False,
  "extra cheese": False
}

toppings["olives"] = False
print(toppings)
"""
"""
stock = {
    "dresses": 25,
    "t-shirts": 50,
    "jeans": 1
}

#stock.pop("caps")
#jeans_stock = stock.pop("jeans")
#print(jeans_stock)
if "jeans" in stock:
    stock.pop("jeans")
print(stock)
"""
"""
routine = {
    "squats": 40,
    "push-ups": 20,
    "lunges": 30
}

routine.pop("lunges")
print(routine)
"""

cast = {
    "Chief": "Bryan Cranston",
    "Nutmeg": "Scarlet Johansson",
    "Rex": "Edward Norton"
}

if "Oracle" in cast:
  cast.pop("Oracle")
print(cast)

"""
scoops = {
    "vanilla": 1,
    "chocolate": 2,
    "hazelnut": 3
}

vanilla = scoops.pop("vanilla")
print(vanilla)
"""
product = {"category": "book", "price": 4.99, "in shop": True} # We can use this instruction to delete a key:value element inside a dictionary
del product["in shop"]

# Checking if a dictionary contains a key
personal_data = {"name": "Mac Miller", "telephone": "0047865791"} # A dictionary
print("name" in personal_data) # To check if a dictionary contains a certain key

# Removing a key-value pair
stock = {"dresses": 25, "t-shirts": 50, "jeans": 1} # A dictionary
if "jeans" in stock: # Good practice to check first if the key exist
  stock.pop("jeans") # Removing the key-value pair
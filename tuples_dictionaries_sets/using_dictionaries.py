"""
actor_bio = {
 "name": "Bill Murray",
 "known for": ["Lost in Translation", "Rushmore"]
}

actor_name = actor_bio["name"]
print(actor_name)
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
ticket = {
 "seat no.": 25,
 "first class": False
}

ticket["first class"] = True
print(ticket)
"""
"""
winner_scores = {
  "first": ("Ted", 50),
  "second": ("Jess", 47)
}

for winner in winner_scores:
  print(winner_scores[winner])
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
"""
participants = {
  "Meg": True,
  "Kim": False,
  "Luis": True,
  "Luis M.": False
}

meg = participants["Meg"]
print(meg)
"""
"""
contents = {
  "ch. 1": "A long-expected party",
  "ch. 2": "The shadow of the past",
  "ch. 3": "Three is company"
}

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
toppings = {
  "olives": True,
  "anchovies": False,
  "extra cheese": False
}

toppings["olives"] = False
print(toppings)
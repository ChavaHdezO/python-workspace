movie_tuples = [("Vertigo", 1958), ("Parasite", 2019)] # List of tuples
vertigo_data = ("Vertigo", 1958) # Tuple
user_data = ("joe_17", ) # Tuples with one value end in a comma separator
vertigo_data = ("Vertigo", 1958, "A. Hitchcock") # Tuples can have as many values as we want
# We can’t update, add or delete values from a tuple (Tuples are immutable)
scores = [("mia", 75), ("lee", 90)]
print(scores[0]) # We can access a tuple values inside a list by it’s index
mia_score = scores[0] # We can save it inside a variable
for user_score in scores:
    print(f"Result: {user_score}") # We can use any kind of loops to loop over a list of tuples
event_tuple = ("Saturday", "21:00", "Anna’s Bday")
print(event_tuple[1]) # We can access a tuple value by their index
def get_scores_data(scores_list): # Tuples allows us to return multiple values from a list
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    return highest_score, lowest_score

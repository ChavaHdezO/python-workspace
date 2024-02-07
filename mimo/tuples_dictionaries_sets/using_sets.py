"""
Sets basics
answers = {"yes", "no"} # Sets don't have indices; This is a set
answers.add("maybe") # Adding a new value to a set
# Elements in sets are unordered
# Add a value duplicated to a set is not allowed, and when we add a duplicated value, nothing happens

print("no" in answers) # We can only check if an element exist in
"""
"""
subscribers = {"jess@mail.com", "meg@mail.com"}
subscribers.add("luke@mail.com")

print(subscribers)

wishlist = {"earpods", "notebook", "handgloves"}
wishlist.add("notebook")
"""
"""
user_answers = ["yes", "yes", "no", "yes"]
print(user_answers[0])
"""
"""
answer_options = {"yes", "no"}
for answer in answer_options: # We can use a for to iterate through one by one element in a set
    print(f"Option: {answer}")
"""
"""
networks = {"May's", "PizzaParty5", "Wi-Free"}

print("Wi-Free" in networks)

for network in networks:
    print(f"Connect to: {network}")
"""
"""
classes = {"Geometry", "Music", "French"}
if "History" in classes: # We can use an if statement to avoid an error when we remove an element
  classes.remove("Music")

print(classes)
"""
arrivals = {"BA1476", "DF2255", "DF2753", "KF3280"}
arrivals.remove("BA1476")
if "DF2255" in arrivals:
    arrivals.remove("DF2255")

print(arrivals)
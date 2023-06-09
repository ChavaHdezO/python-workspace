"""
answers = {"yes", "no"}
answers.add("yes")

print("no" in answers)
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
for answer in answer_options:
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
if "History" in classes:
  classes.remove("Music")

print(classes)
"""
arrivals = {"BA1476", "DF2255", "DF2753", "KF3280"}
arrivals.remove("BA1476")
if "DF2255" in arrivals:
    arrivals.remove("DF2255")

print(arrivals)
"""
friends = {"Emma", "Jen", "Rob", "Ed"}
chat = {"Jen", "Ed"}
study_group = {"Emma", "Lisa"}

print(len(friends))
print(chat.issubset(friends))
are_friends = study_group.issubset(friends)
print(are_friends)

invitations = {"Meg", "Alex", "Lee"}
print(f"{len(invitations)} invitations sent")

animals = {"whale", "dog", "cat", "giraffe"}
pets = {"dog", "cat"}

print(pets.issubset(animals))

classmates = {"Sue", "Luke", "Paul"}
friends = {"Don", "Sue", "Luke"}

print(classmates.intersection(friends))
"""

classmates = {"Sue", "Paul"}
friends = {"Don", "Sue"}

print(classmates.union(friends))
friends_not_classmates = friends.difference(classmates)

print(friends_not_classmates)
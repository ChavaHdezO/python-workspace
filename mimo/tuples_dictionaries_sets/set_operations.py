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

# Subset
friends = {"Lena", "Rob", "Jon", "Ed"} # We can get the size of a set with the len() function
print(len(friends))
best_friends = {"Lena", "Jon"} # Subset of a friends
print(best_friends.issubset(friends)) # To check if a set is a subset of a set

# Union and Intersections
classmates = {"Sue", "Paul"} # We can join two sets in one set
friends = {"Don", "Sue"}
print(classmates.union(friends))
classmates = {"Sue", "Luke", "Paul"} # We can create a set of the common elements presents in two sets
friends = {"Don", "Sue", "Luke"}
print(classmates.intersection(friennds))

# Difference
classmates = {"Sue", "Paul"} # To get a set of elements that are presents in the first set, but not in the second set
friends = {"Don", "Sue"}
print(classmates.difference(friends))

postcodes = {"SW1A", "SY3", "B44"} # This is a set
# Sets can't store duplicated values

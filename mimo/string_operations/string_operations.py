schedule = ["ballet", "swimming"] # List of strings
print("ballet" in schedule) # Get True or False if the item is in the list
# Lists can have multiple types of data
signups = ["44-22-4-11"]
signups_list = signups.split("-") # Splits in items the list using the given value as a separator
# Default separator for split() function is whitespace
rep = "Yes!"
rep = rep.replace("!", "?") # Replace the first string with the second string in the variable
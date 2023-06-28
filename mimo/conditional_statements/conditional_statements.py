read = 5
unread = 4

if unread != 0:
  print(f"You have {unread} messages")
else:
  print(f"No unread messages. Check your {read} messages")

actualPass = "abc123"
enteredPass = "Abc123"

if actualPass == enteredPass:
  print("Login successful")
else:
  print("Incorrect credentials. Please try again")
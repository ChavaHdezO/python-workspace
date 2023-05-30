"""
def onboard_passengers(bookings):
  counter = 1
  while counter <= bookings:
    print(f"Passenger {counter} on board")
    counter += 1

onboard_passengers(4)
"""
"""
def display_progress(total_files):
  for i in range(total_files):
    print(f"Downloading file {i} out of {total_files}")

display_progress(3)
"""
"""
def do_countdown(counter):
  while counter > 0: 
    print(counter)
    counter -= 1
  print("Go!")  

do_countdown(3)
"""
"""
def display_stars(rows):
  counter = 0
  while counter < rows:
    print("***")
    counter += 1

display_stars(2)
"""
"""
def show_progress(total):
  for i in range(total):
    print(f"Installing next update")

show_progress(3)
"""
"""
def repeat_message():
  for i in range(4):
    print("Polly wants a cracker")

repeat_message()
"""
"""
def show_notifications(messages):
 for i in range(messages):
  print("Failed to send message")

show_notifications(3)
"""
"""
def function_example(total):
  counter = 0
  while counter < total:
    counter += 1
    print(f"Hola {counter}")

function_example(4)
"""
"""
def function_example(total):
  for i in range(total):
    print(f"Hola {i + 1}")

function_example(4)
"""
"""
def halve_prices(cart):
  for price in cart:
    print(f"New price: {price/2}")

cart_list = [5, 20, 8]
halve_prices(cart_list)
"""
"""
def display_players(team):
  number = 1
  for name in team:
    print(f"Player {number}: {name}")

team_1 = ["Kim", "Lee"]
team_2 = ["Meg", "Jo"]
display_players(team_1)
"""
"""
def show_next_track():
  playlist = ["Hey Jude", "Helter Skelter", "Something"]
  for track in playlist:
    print(f"Next up: {track}")

show_next_track()
"""
"""
def show_next_track(playlist):
  for track in playlist:
    print(f"Next up: {track}")

beatles = ["Hey Jude", "Helter Skelter", "Something"]
show_next_track(beatles)
"""
"""
def show_next_track(playlist):
  for track in playlist:
    print(f"Next up: {track}")

beatles = ["Hey Jude", "Helter Skelter", "Something"]
beethoven = ["Symphony No. 1", "Symphony No. 9"]

show_next_track(beethoven)
show_next_track(beatles)
"""
"""
def add_to_savings(amount):
  total_savings = 70
  total_savings += 10
  print(f"Savings: {total_savings + amount}")

add_to_savings(20)
"""
"""
day_time = "morning"

def show_question():
  print(f"How are you this {day_time}?")

show_question()
"""
"""
bills = 1000

def calculate_spendings():
  rent = 1000
  print(f"Total: {rent + bills}")

calculate_spendings()
"""
"""
alarm_time = 7

def set_alarm():
  print(f"New alarm set for {alarm_time}AM")

set_alarm()
"""
"""
def display_instructions(add_sugar):
  if add_sugar:
    print("Enter amount of sugar")
  print("Select coffee type")

display_instructions(False)
"""
"""
def has_red(rgb_values):
  if rgb_values[0] > 0:
    print("Red is in the mix!")

rgb = [153, 255, 51]
has_red(rgb)
"""
"""
def change_battery_color(level):
  if level <= 10:
    print("Color: red")
  elif level <= 20:
    print("Color: yellow")
  else:
    print("Color: green")

change_battery_color(15)
"""
"""
def display_programme(movies):
  print(movies)

movie_list = ["Alien", "Moon"]
display_programme(movie_list)
"""
"""
def add_sports(plans):
  plans[0] = "jogging"

plans = ["reading", "brunch with Meg", "cooking", "netflix"]
add_sports(plans)
print(plans)
"""
"""
def is_valid(parts):
  print(len(parts) == 2)

email = "laurie@gmail.com"
user_and_domain = email.split("@")
is_valid(user_and_domain)
"""
"""
def onboard_passengers(bookings):
  counter = 0
  while counter <= bookings:
    counter += 1
  print("Onboarding passenger")
    

onboard_passengers(4)
"""
"""
def help_customers(customers):
  counter = 1
  while counter < customers:
    print(f"Customer no.{counter} go to the next free desk")
    counter += 1

help_customers(3)
"""
"""
def show_instructions(ingredients):
  for item in ingredients:
    print(f"Stir in: {item}")

cake = ["flour", "softened butter", "milk", "sugar", "eggs"]
hot_chocolate = ["milk", "chocolate"]
show_instructions(hot_chocolate)
"""
"""
def show_programme(day):
  for event in day:
    print(f"Today: {event}")

monday = ["Swan Lake", "Ravel - Piano Concerto"]
tuesday = ["La Boheme"]

show_programme(monday)
show_programme(tuesday)
"""
def show_notifications(messages):
  for i in range(messages):
    print("Failed to send message")

show_notifications(3)
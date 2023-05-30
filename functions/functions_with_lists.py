"""
def is_multiplayer(players):
  print(len(players) == 2)

players = ["Amy", "Jay"]
is_multiplayer(players)
"""
"""
def display_programme(movies):
  print(f"Airing tonight: {movies}")

movie_list = ["Alien", "Moon"]
display_programme(movie_list)
"""
"""
def display_programme(movies):
  print("Airing tonight:")
  print(movies)

movie_list = ["Alien", "Moon"]
display_programme(movie_list)
"""
"""
def count_passengers(passengers):
  print(len(passengers))

passengers = ["June", "Sam", "Lee"]
count_passengers(passengers)
"""
"""
def is_booked(passengers):
  print(len(passengers) > 4)

passengers = ["June", "Sam", "Lee"]
is_booked(passengers)
"""
"""
def get_winner(top_players):
  winner = top_players[0]
  print(f"Game winner: {winner}")

top_players = ["Jay", "Meg", "Cy"]
get_winner(top_players)
"""
def update_first_place(leaderboard, player):
  leaderboard[0] = player
  return leaderboard

leaderboard = ["Jay", "Meg", "Cy"]
leaderboard = update_first_place(leaderboard, "Lena")
print(leaderboard)
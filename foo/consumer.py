import requests

class Game:
    def __init__(self, name):
        self.name = name
        self.custom_name = "Krodun"

    def get_custom_name(self):
        return self.custom_name

# Path from https://www.freetogame.com/api-doc
api_url = "https://www.freetogame.com/api/games?platform=pc"

# Get the response from the API
response = requests.get(api_url)

# Get the JSON data from the response
data = response.json()

# Create a list of Game objects
games = []

# Iterate over the data and create a Game object for each item
for game in data:
    games.append(Game(game["title"]))

# Print the name of each game
for game in games:
    print(game.get_custom_name())


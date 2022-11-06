import requests
from datetime import datetime
from time import sleep
import logging
from pathlib import Path

LOG_FILE = Path("/output/python.log")
LOG_LEVEL = logging.INFO
LOG_FILEMODE = "a"
LOG_FMT = "%(asctime)s %(levelname)-8s %(message)s"
LOG_DATE_FMT = "%Y-%m-%d %H:%M:%S"

class Game:
    def __init__(self, name):
        self.name = name
        self.custom_name = "Krodun"

    def get_custom_name(self):
        return self.custom_name

def log():
    logging.basicConfig(
        filename=LOG_FILE,
        format=LOG_FMT,
        datefmt=LOG_DATE_FMT,
        level=LOG_LEVEL,
        filemode=LOG_FILEMODE
    )
    logging.info("Starting ...")

    sleep(5)

    logging.info("Done.")
    print("test print")

def main():
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

    log()

if __name__ == "__main__":
    main()


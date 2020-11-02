import cowsay
import json
from os import system, name
import random

CHARACTERS = ["beavis", "cheese", "daemon", "cow", "dragon", "ghostbusters", "kitty", "meow", "milk", "stegosaurus",
              "stimpy", "turkey", "turtle", "tux"]


def get_character():
    """This function chooses the character for cowsay

    Returns:
        str - cowsay character
    """
    return random.choice(CHARACTERS)


def get_quote():
    """
    This function is responsible for returning a quote (str)
    """
    with open("quotes.json", "r") as file:
        quotes = json.load(file)
        quote_of_day = " ".join(random.choice(quotes))
        return quote_of_day



if __name__ == "__main__":
    character = get_character()
    print(f"Character name:\t{character}")
    print("Quote of the day:\n\n\n")
    getattr(cowsay, character)(get_quote())

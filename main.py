import cowsay
import json
from os import system, name
from random import choice

CHARACTERS = ["beavis", "cheese", "daemon", "cow", "dragon", "ghostbusters", "kitty", "meow", "milk", "stegosaurus",
              "stimpy", "turkey", "turtle", "tux"]


def get_character():
    """This function chooses the character for cowsay

    Returns:
        str - cowsay character
    """
    return CHARACTERS[-1]


def get_quote():
    with open("quotes.json", "r") as file:
        quotes = json.load(file)
        quote_of_day = " ".join(choice(quotes))
        return quote_of_day



if __name__ == "__main__":
    print("Quote of the day:\n\n\n")
    getattr(cowsay, get_character())(get_quote())

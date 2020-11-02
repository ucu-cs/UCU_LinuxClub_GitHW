import cowsay
import json
<<<<<<< HEAD
from os import system, name
from random import choice
=======
import random

>>>>>>> main

CHARACTERS = ["beavis", "cheese", "daemon", "cow", "dragon", "ghostbusters", "kitty", "meow", "milk", "stegosaurus",
              "stimpy", "turkey", "turtle", "tux"]


def get_character():
    """This function chooses the character for cowsay
    Returns:
        str - cowsay character
    """
    character = random.choice(CHARACTERS)
    return character


def get_quote():
    """
<<<<<<< HEAD
    This function is responsible for returning a quote (str)
    """
    with open("quotes.json", "r") as file:
        quotes = json.load(file)
        quote_of_day = " ".join(choice(quotes))
        return quote_of_day



if __name__ == "__main__":
    character = get_character()
    print(f"Character name:\t{character}")
    print("Quote of the day:\n\n\n")
    getattr(cowsay, character)(get_quote())
=======
    Responsible for getting a quote.
    Args:
    Returns:
        str - a quote
    """
    return "This is quote from latest master branch! Random quotes coming soon!"

if __name__ == "__main__":
    character = get_character()
    print(f"{character.capitalize()} says:\n\n\n")

    getattr(cowsay,character)(get_quote())


>>>>>>> main

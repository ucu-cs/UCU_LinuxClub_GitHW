from os import system, name
import cowsay
import json
from random import choice

CHARACTERS = ["beavis", "cheese", "daemon", "cow", "dragon", "ghostbusters", "kitty", "meow", "milk", "stegosaurus",
              "stimpy", "turkey", "turtle", "tux"]


def get_character():
    """This function chooses the character for cowsay

    Returns:
        str - cowsay character
    """
    return choice(CHARACTERS)

def get_quote():
    """
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


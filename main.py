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
    return choice(CHARACTERS)


def get_quote():
    """
    Responsible for getting a quote.
    Args:

    Returns:
        str - a quote
    """
    with open("quotes.json", "r") as file:
        quotes = json.load(file)
        quote_of_day = " ".join(choice(quotes))
        return quote_of_day

if __name__ == "__main__":
    character = get_character()
    print(f"{character.capitalize()} says:\n\n\n")
    print("Quote of the day:\n\n\n")
    getattr(cowsay, get_character())(get_quote())

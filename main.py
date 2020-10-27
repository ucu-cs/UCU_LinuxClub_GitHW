from os import system, name
import cowsay
import json

CHARACTERS = ["beavis", "cheese", "daemon", "cow", "dragon", "ghostbusters", "kitty", "meow", "milk", "stegosaurus",
              "stimpy", "turkey", "turtle", "tux"]


def get_character():
    """This function chooses the character for cowsay

    Returns:
        str - cowsay character
    """
    return CHARACTERS[-1]

def get_quote():
    return "This is quote from latest master branch! Random quotes coming soon!"

if __name__ == "__main__":
    print("Quote of the day:\n\n\n")
    getattr(cowsay,get_character())(get_quote())


from Classes.Inventory import Inventory
from Classes.Item import Item
from Classes.SubClasses.Human import Human

import time
import rich
from rich import print as rprint
from rich.console import *
from rich import console

def mainMenu():
    rprint("Welcome to the game!")
    rprint("What would you like to do?")
    rprint("1. Start a new game")
    rprint("2. Load a game")
    rprint("3. Exit")
    choice = input("#: ")
    if choice == "1":
        startGame()
    elif choice == "2":
        loadGame()
    elif choice == "3":
        exit()


def startGame():
    Console().clear()
    name = input("What is your name?: ")
    playerInventory = Inventory(5)
    player = Human(name, "Your not [italic] That Attractive[/italic]", playerInventory, 20, None, None, 0, 0)
    time.sleep(10)
    
    
    
    
def inspectAny(object):
    return object.inspect()
    





mainMenu()


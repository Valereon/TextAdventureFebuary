from Classes.Inventory import Inventory
from Classes.Item import Item
from Classes.SubClasses.Human import Human
from Classes.SubClasses.Enemy import Enemy

from rich import print as rprint

import os

entities = []
gameMap = ["F", "F", "F\n",
           "F", "F", "F\n",
           "F", "F", "F\n",
           "F", "F", "F\n",
           "F", "F", "F\n",]

def collisions():
    for i in range(len(entities) - 1):
        if entities[i].x == entities[i + 1].x and entities[i].y == entities[i + 1].y:
            print("Collision with entity", entities[i].name, "and entity", entities[i + 1].name)
        

def render():
    os.system("clear")
    for i in range(len(gameMap)):
        print(gameMap[i], end="")

def playerInput():
    pass

def aiMovement():
    pass





while True:
    collisions()
    render()
    playerInput()
    aiMovement()









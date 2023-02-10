from Classes.Item import Item
import json


class CraftingSystem():
    def __init__(self, name, description, TypeOfCrafting, playerInventory):
        self.name = name
        self.description = description
        self.TypeOfCrafting = TypeOfCrafting
        self.playerInventory = playerInventory
        
        with open("Data/Items.json", "r") as f:
            self.craftingRecipes = json.load(f)
            
        if self.TypeOfCrafting == "Crafting Table":
            self.craftingTable = True
        elif self.TypeOfCrafting == "Furnace":
            self.furnace = True
        elif self.TypeOfCrafting == "Anvil":
            self.anvil = True
        elif self.TypeOfCrafting == "Forge":
            self.forge = True
        elif self.TypeOfCrafting == "InventoryCrafting":
            self.inventoryCrafting = True


    def craft(self, items : list[Item], whatToCraft : Item):
        self.items = items
        self.craftingRecipes[whatToCraft.name]

    def onCraft(self, product : Item):
        print(f"You have crafted {self.name}.")

    def onDrop(self, x, y):
        print(f"You have dropped {self.name}.")
        self.x = x
        self.y = y
    
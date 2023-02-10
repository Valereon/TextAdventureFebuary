from Classes.Item import Item
from Classes.Systems.StarSystem import StarSystem

class Armor(Item, StarSystem):
    def __init__(self,name,description,worth,overAllDefense,rarity = "Common", stars = 0, xp = 0, level = 0, xpForNextLevel = 100):
        Item.__init__(self, name, description, worth)
        StarSystem.__init__(self, "Common", 0, 0, 0, 100)
        self.overAllDefense = overAllDefense
        self.helmet = self.name + " Helmet"
        self.chestplate = self.name + " Chestplate"
        self.leggings = self.name + " Leggings"
        self.boots = self.name + " Boots"

        self.helmetDefense = self.overAllDefense * 0.25
        self.chestplateDefense = self.overAllDefense * 0.35
        self.leggingsDefense = self.overAllDefense * 0.25
        self.bootsDefense = self.overAllDefense * 0.15
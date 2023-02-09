from Classes.SubClasses.Weapon import Weapon

class Armor(Weapon):
    def __init__(self, name: str, description: str, worth: int, damage: int, rarity: int, stars: int, level: int, xp: int, xpForNextLevel: float, durability: int, repairItems: list, overAllDefense : int):
        super().__init__(name, description, worth, damage, rarity, stars, level, xp, xpForNextLevel, durability, repairItems)
        self.overAllDefense = overAllDefense
        self.helmet = self.name + " Helmet"
        self.chestplate = self.name + " Chestplate"
        self.leggings = self.name + " Leggings"
        self.boots = self.name + " Boots"

        self.helmetDefense = self.overAllDefense * 0.25
        self.chestplateDefense = self.overAllDefense * 0.35
        self.leggingsDefense = self.overAllDefense * 0.25
        self.bootsDefense = self.overAllDefense * 0.15
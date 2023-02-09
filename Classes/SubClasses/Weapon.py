from Classes.Item import Item
class Weapon(Item):
    """A subclass of Item that represents a weapon.

    Args:
        Item (Class): Initailizes The Weapon With Attributes From Item.
    """  
    def __init__(self, name: str, description: str, worth: int, damage: int, rarity: int, stars: int, level: int, xp: float, xpForNextLevel: float, durability: int, repairItems: list[Item]):
        """Initializes a Weapon object.

        Args:
            name (Super(String)): The name of the weapon.
            description (Super(String)): Description of the weapon. to be displayed on inspect.
            worth (Super(Int)): The worth of the weapon. 
            damage (Int): The damage of the weapon.
            rarity (String): The rarity of the weapon on a scale of uncommon to legendary.
            stars (Int): The number of stars the weapon has. as in the star level
            level (Int): The level of the weapon.
            durability (Int): The durability of the weapon.
            repairItems (Items[]): The items needed to repair the weapon.
        """
        super().__init__(name, description, worth)
        self.damage = damage
        self.rarity = rarity
        self.stars = stars
        self.level = level
        self.durability = durability
        self.repairItems = repairItems
        self.xp = xp
        self.xpForNextLevel = xpForNextLevel
        self.maxLevelPerStar = 10
        
    
    def __str__(self):
        return f"{self.name}: {self.description}"
    
    def xpCheck(self):
        if self.xp >= self.xpForNextLevel:
            self.levelUp()
    
    def addXP(self, XP):
        self.xp += XP
        self.xpCheck()
    
    def levelUp(self):
        self.level += 1
        self.xpForNextLevel *= 1.5
        
    def starLevelUp(self):
        if self.level >= self.maxLevelPerStar:
            self.stars += 1
            self.damage *= 1.15
            self.durability *= 1.25
            self.level = 0
            self.xpForNextLevel *= 1.2
    
    def randomizeRepairItems(self):
        pass
    

    def repair(self, item):
        if item in self.repairItems:
            self.durability += 1
            self.repairItems.remove(item)
            print(f"Repaired {self.name} with {item.name}")
        else:
            print(f"{item.name} is not a repair item for {self.name}")
    
    def reduceDurability(self, amount):
        self.durability -= amount
        if self.durability <= 0:
            self.durability = 0
            print(f"{self.name} has broken!")
    
    def inspect(self):
        print(f"{self.name}: {self.description} \nDamage: {self.damage} \nRarity: {self.rarity} \nStars: {self.stars} \nLevel: {self.level} \nDurability: {self.durability} \nRepair Items: {self.repairItems}")
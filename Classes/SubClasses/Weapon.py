from Classes.Item import Item
from Classes.Systems.StarSystem import StarSystem
class Weapon(Item, StarSystem):
    """A subclass of Item that represents a weapon.

    Args:
        Item (Class): Initailizes The Weapon With Attributes From Item.
    """  
    def __init__(self, name: str, description: str, worth: int, damage: int,
                durability: int, repairItems: list[Item] = None,
                rarity: str = "Common", stars: int = 0, xp: int = 0,
                level: int = 0, xpForNextLevel: int = 100):

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
        self.rarity = rarity
        self.stars = stars
        self.xp = xp
        self.level = level
        self.xpForNextLevel = xpForNextLevel         
        self.damage = damage
        self.durability = durability
        self.repairItems = repairItems
        Item.__init__(name, description, worth)
        StarSystem.__init__(self, self.rarity, self.stars, self.xp, self.level, self.xpForNextLevel)
        
        
        
        
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
        
from Classes.Item import Item
from Classes.SubClasses.Armor import Armor

class Inventory:
    """Makes an inventory object.
    """
    def __init__(self, capacity=None):
        """Initializes an Inventory object."""
        self.items = []
        self.Descriptions = []
        self.capacity = capacity

    def initArmorSlots(self, headSlot=None, chestSlot=None, legsSlot=None, feetSlot=None, weaponSlot=None, offHandSlot=None, ringSlot=None, necklaceSlot=None):
        """Init the Armor slots. for the entitity with a inventory. object attached to it."""
        self.headSlot = headSlot
        self.chestSlot = chestSlot
        self.legsSlot = legsSlot
        self.feetSlot = feetSlot
        self.weaponSlot = weaponSlot
        self.offHandSlot = offHandSlot
        self.ringSlot = ringSlot
        self.necklaceSlot = necklaceSlot

    
    def __str__(self):
        """Returns the string representation of the inventory."""
        print(f"Capacity:{len(self.items)}/{self.capacity}")
        
        for i in range(len(self.items) - 1):
            print("\t" + self.items[i].__str__() + " " + "\t" + self.items[i + 1].__str__())
    
    
    def populateInventory(self, items=None[Item]):
        """Populates the inventory with items.
        
        Args:
            items (Items[]=None items to populate the inventory with.
        """
        if self.checkIfFull():
            print("Inventory is full.")
            return
        for item in items:
            self.items.append(item.name)
            self.Descriptions.append(item.description)
    
    def addItem(self, item):
        """Adds an item to the inventory.
        
        Args:
            item (Item=None item to add to the inventory.
        """
        self.items.append(item)
    
    def removeItem(self, item):
        """Removes an item from the inventory.
        
        Args:
            item (Item=None item to remove from the inventory.
        """
        self.items.remove(item)
    
    
    def getItem(self, item):
        """Gets an item from the inventory.
        
        Args:
            item (Item=None item to get from the inventory.
        """
        return self.items[item]
    
    def checkIfFull(self):
        """Checks if the inventory is full.
        
        Returns:
            boo=None if the inventory is full, False if it is not.
        """
        if len(self.items) >= self.capacity:
            return True
        else:
            return False

    
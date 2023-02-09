from Classes.ItemClass import Item

class Inventory:
    """Makes an inventory object.
    """
    def __init__(self, capacity : int | None):
        """Initializes an Inventory object."""
        self.items = []
        self.Descriptions = []
        self.capacity = capacity

    
    def __str__(self):
        """Returns the string representation of the inventory."""
        return "Inventory\n" + f"Capcaity:{len(self.items)}/{self.capacity}\n" + "\n".join(self.items) + "\n" + "\n".join(self.Descriptions)
    
    
    def populateInventory(self, items : list[Item]):
        """Populates the inventory with items.
        
        Args:
            items (Items[]): The items to populate the inventory with.
        """
        for item in items:
            self.items.append(item.name)
            self.Descriptions.append(item.description)
    
    def addItem(self, item):
        """Adds an item to the inventory.
        
        Args:
            item (Item): The item to add to the inventory.
        """
        self.items.append(item)
    
    def removeItem(self, item):
        """Removes an item from the inventory.
        
        Args:
            item (Item): The item to remove from the inventory.
        """
        self.items.remove(item)
    
    
    
    
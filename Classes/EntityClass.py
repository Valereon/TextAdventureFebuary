from Classes.InventoryClass import Inventory
from Classes.AIClass import AI
class Entity:
    
    """The Entity class is the base class for all entities in the game."""
    def __init__(self, name, description, inventory : Inventory | None, ai : AI | None, x, y):
        """Initializes an Entity object.

        Args:
            name (String): The name of the entity.
            description (String): Description of the entity. to be displayed on inspect.
            inventory (Inventory): The inventory of the entity.
            ai (Ai/None): The type of ai the entity has.
            x (Int): xCoordaite of the entity.
            y (Int): Y coordinate of the entity.
        """
        self.name = name
        self.description = description
        self.inventory = inventory
        self.ai = ai
        self.x = x
        self.y = y
        
    
    def distanceFromPlayer(self, player):
        """Calculates the distance from the player.

        Args:
            player (Entity): The player.

        Returns:
            int: The distance from the player.
        """
        return (self.x - player.x) + (self.y - player.y)

    
    def moveOnMap(self, x, y):
        """Moves the entity on the map.

        Args:
            x (Int): The x coordinate to move to.
            y (Int): The y coordinate to move to.
        """
        self.x = x
        self.y = y
    
    
        
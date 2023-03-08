from Classes.Inventory import Inventory
class Entity:
    
    """The Entity class is the base class for all entities in the game."""
    def __init__(self, name, description, x, y, inventory = None):
        """Initializes an Entity object.

        Args:
            name (String): The name of the entity.
            description (String): Description of the entity. to be displayed on inspect.
            inventory (Inventory): The inventory of the entity.
            x (Int): xCoordaite of the entity.
            y (Int): Y coordinate of the entity.
        """
        self.name = name
        self.description = description
        self.inventory = inventory
        self.x = x
        self.y = y
    
    
    def inspect(self):
        return f"{self.name}: {self.description}"
        
        
    
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
    def onCollision(self, entity):
        """When two entites collide.

        Args:
            entity (Entity): The Enitiy Base Class
        """        
        pass

            
    
        
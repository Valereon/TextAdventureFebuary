from Classes.Entity import Entity

class Human(Entity):
    def __init__(self, name, description, inventory, ai, health, currentWeapon, armor, x, y):
        """Initializes a Human object From the Entity Class.

        Args:
            name (Super(String)): The name of the entity.
            description (Super(String)): Description of the entity. to be displayed on inspect.
            inventory (Super(Inventory)): The inventory of the entity.
            ai (Super(Ai/None)): The type of ai the entity has.
            health (Int): The health of the entity.
            currentWeapon (Weapon): The current weapon the entity is holding.
            armor (Armor): The armor the entity is wearing.
            x (Super(Int)): xCoordaite of the entity.
            y (Super(Int)): Y coordinate of the entity.
        """
        super().__init__(name, description, inventory, ai, x, y)

        self.health = health
        self.currentWeapon = currentWeapon
        self.armor = armor
        
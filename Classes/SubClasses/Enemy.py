from Classes.Entity import Entity

class Enemy(Entity):
    def __init__(self, name, description, inventory, ai, health, defense, armor, x, y):
        super().__init__(name, description, inventory, ai, x, y)
    
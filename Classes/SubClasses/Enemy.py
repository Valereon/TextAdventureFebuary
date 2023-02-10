from Classes.Entity import Entity

class Enemy(Entity):
    def __init__(self, name, description, inventory, ai, health, defense, armor, speed, x, y):
        super().__init__(name, description, inventory, ai, x, y)
        self.health = health
        self.defense = defense
        self.armor = armor
        self.speed = speed
        
    def moveTowardsPlayer(self, player, enemy):
        if player.x > self.x:
            self.x += self.speed
        elif player.x < self.x:
            self.x -= self.speed
        if player.y > self.y:
            self.y += self.speed
        elif player.y < self.y:
            self.y -= self.speed
    
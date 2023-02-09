from Classes.Item import Item

class Food(Item):
    def __init__(self, name, description, value, health):
        self.health = health
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHealth: {}".format(self.name, self.description, self.value, self.health)

    def use(self, player):
        player.health += self.health
        print("You eat the {}, and your health is now {}.".format(self.name, player.health))
        return True
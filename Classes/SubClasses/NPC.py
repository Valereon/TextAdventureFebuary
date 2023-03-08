from Classes.Entity import Entity

class NPC(Entity):
    def __init__(self, name, description, x, y, dialogue):
        super().__init__(name, description, x, y)
        self.dialogue = dialogue
        

        
    




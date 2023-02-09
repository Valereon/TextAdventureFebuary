class Item:
    def __init__(self, name, description, worth):
        """Initializes an Item object.

        Args:
            name (String): The name of the item.
            description (String): Description of the item. to be displayed on inspect.
            worth (Int): The worth of the item.
        """
        self.name = name
        self.description = description
        self.worth = worth

    def __str__(self):
        return f"{self.name}: {self.description}"

    def onTake(self):
        print(f"You have picked up {self.name}.")

    def onDrop(self, x, y):
        print(f"You have dropped {self.name}.")
        self.x = x
        self.y = y
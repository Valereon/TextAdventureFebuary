from Classes.InventoryClass import Inventory
from Classes.ItemClass import Item



inv = Inventory(10)
    


item1 = Item("Item1", "This is item 1", 10)
item2 = Item("Item2", "This is item 2", 10)
item3 = Item("Item3", "This is item 3", 10)
item4 = Item("Item4", "This is item 4", 10)
item5 = Item("Item5", "This is item 5", 10)
item6 = Item("Item6", "This is item 6", 10)
item7 = Item("Item7", "This is item 7", 10)





inv.populateInventory([item1, item2, item3, item4, item5, item6, item7])

print(inv.__str__())

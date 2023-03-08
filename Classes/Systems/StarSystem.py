class StarSystem:
    def __init__(self, rarity = "Common", stars = 0,
                level = 0, xp = 0, xpForNextLevel = 100):

        self.rarity = rarity
        self.stars = stars
        self.level = level
        self.xp = xp
        self.xpForNextLevel = xpForNextLevel
        self.maxLevelPerStar = 10
        self.maxStars = 5
    
    def xpCheck(self):
        if self.xp >= self.xpForNextLevel:
            self.levelUp()
    
    def addXP(self, XP):
        self.xp += XP
        self.xpCheck()
    
    def levelUp(self):
        self.level += 1
        self.xpForNextLevel *= 1.5
        
    def starLevelUp(self):
        if self.level >= self.maxLevelPerStar:
            self.stars += 1
            self.durability *= 1.25
            self.level = 0
            self.xpForNextLevel *= 1.5
    def rarityColoring(self):
        if self.rarity == "Common":
            return "White"
        elif self.rarity == "Uncommon":
            return "Green"
        elif self.rarity == "Rare":
            return "Blue"
        elif self.rarity == "Epic":
            return "Purple"
        elif self.rarity == "Legendary":
            return "Gold"
        else:
            return "White"        
        

 
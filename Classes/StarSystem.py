class StarSystem:
    def __init__(self, rarity, stars, level, durability, repairItems, xp, xpForNextLevel):
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

 
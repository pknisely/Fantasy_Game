# Import Weapon Class
import weapon

# Player class definition
class Player:
    def __init__(self, name, race, sex):

# Assign the name to the name variable
        self.name = name

# Assign race to the race variable
        self.race = race

# Based on race, set appropriate stats and starting inventory
        if race == 'Elf':
            bow = weapon.Weapon('bow', 2, 5)
            self.inventory = {'bow': bow}
            self.stats = [1, 4, 4]
        elif race == 'Dwarf':
            axe = weapon.Weapon('axe', 4, 1)
            self.inventory = {'axe': axe}
            self.stats = [3, 1, 3]
        elif race == 'Human':
            sword = weapon.Weapon('sword', 2, 2)
            self.inventory = {'sword': sword}
            self.stats = [2, 3, 2]
        elif race == 'Orc':
            mace = weapon.Weapon('mace', 5, 1)
            self.inventory = {'mace': mace}
            self.stats = [4, 2, 1]

# Assign proper sex
        if sex == 'M':
            self.sex = 'Male'
        if sex == 'F':
            self.sex = 'Female'

# Put character in initial game location, City block 2, 1
#        self.location = City_2_1

# Print character's stats
 
    def getStats(self):
        return 'Strength:', self.stats[0], 'Speed:', self.stats[1], 'Intelligence', self.stats[2]

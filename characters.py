# Player class definition
class Character():
    def __init__(self, name, race, sex):

# Assign the name to the name variable
        self.name = name

# Assign race to the race variable
        self.race = race

# Based on race, set appropriate stats and starting inventory
        if race == 1:
            sword = weapon.Weapon('sword', 2, 2)
            self.inventory = {'sword': sword}
            self.stats = [2, 3, 2]
        elif race == 2:
            bow = weapon.Weapon('bow', 2, 5)
            self.inventory = {'bow': bow}
            self.stats = [1, 4, 4]
        elif race == 3:
            axe = weapon.Weapon('axe', 4, 1)
            self.inventory = {'axe': axe}
            self.stats = [3, 1, 3]
        elif race == 4:
            mace = weapon.Weapon('mace', 5, 1)
            self.inventory = {'mace': mace}
            self.stats = [4, 2, 1]

# Assign proper sex
        if sex == 'M':
            self.sex = 'Male'
        if sex == 'F':
            self.sex = 'Female'

# Character has no location initially
        self.location = None

# Print character's stats
    def get_stats(self):
        return 'Strength:', self.stats[0], 'Speed:', self.stats[1], 'Intelligence', self.stats[2]

class Player(Character):


class NPC(Character):

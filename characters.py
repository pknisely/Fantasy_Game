import items

# Player class definition
class Character():
    def __init__(self, name, race, sex, location):

# Assign the name to the name variable
        self.name = name

# Assign race to the race variable
        self.race = race

# Based on race, set appropriate stats and starting inventory
        if race == 1:
            sword = items.Weapon('sword', 2, 2)
            self.inventory = {'sword': sword}
            self.stats = [2, 3, 2]
        elif race == 2:
            bow = items.Weapon('bow', 2, 5)
            self.inventory = {'bow': bow}
            self.stats = [1, 4, 4]
        elif race == 3:
            axe = items.Weapon('axe', 4, 1)
            self.inventory = {'axe': axe}
            self.stats = [3, 1, 3]
        elif race == 4:
            mace = items.Weapon('mace', 5, 1)
            self.inventory = {'mace': mace}
            self.stats = [4, 2, 1]

# Assign proper sex
        if sex == 'M':
            self.sex = 'Male'
        if sex == 'F':
            self.sex = 'Female'

# Character has no location initially
        self.location = location

# Print character's stats
    def get_stats(self):
        return 'Strength:', self.stats[0], 'Speed:', self.stats[1], 'Intelligence', self.stats[2]

class Player(Character):
    def __init__(self, name, race, sex, location):
        Character.__init__(self, name, race, sex, location)

class NPC(Character):
    def __init__(self, name, race, sex, location):
        Character.__init__(self, name, race, sex, location)


def create_character():
    name = input("Type your character\'s name: ")
    print()
    print("Choose from the following races:")
    print("1 - Human")
    print("2 - Elf")
    print("3 - Dwarf")
    print("4 - Orc")
    print()
    race = int(input("Enter your character\'s race: "))
    while race > 4 or race < 1:
        print("You must enter a numerical value between 1 and 4")
        race = int(input("Enter your character\'s race: "))
    sex = input("Enter your character\'s sex: ")
    while sex != "M" and sex != "F":
        print("You must enter either M or F for sex.")
        sex = input("Enter your character's sex: ")        
    return Player(name, race, sex, 'C_1_2')

import player
import weapon
import location

def main():
    print('Welcome to the game.')
    print('Create a character to begin.')

    player = createCharacter()
    print(player.name)
    print(player.race)
    print(player.sex)
    print(player.inventory)
    print(player.getStats())

def createCharacter():
    print('****FIX WITH MENUS****')
    name = input('Enter your character\'s name: ')
    race = input('Enter your character\'s race: ')
    sex = input('Enter your character\'s sex: ')
    return player.Player(name, race, sex)

    
main()

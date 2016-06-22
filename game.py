import characters
import items
import places

def main():
    print('*****Welcome to Moonfall*******')
    print()
    print('Moonfall is a text based fantasy adventure.')
    print()
    input('Press enter to begin playing.')
    print()
    player = characters.create_character()
    launch(player)
#   print(player.name)
#   print(player.race)
#   print(player.sex)
#   print(player.inventory)
#   print(player.get_stats())


def launch(player):
    print(places.city_locations[player.location].title)
    print()
    print(places.city_locations[player.location].current_desc)
    get_action()

def get_action():
    action = input(' >> ')
    while action != 'q':
        action = input(' >> ')
             
main()

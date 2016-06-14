import player
import weapon
import location
import citygate

def main():
    print("Welcome to Moonfall.")
    print("A text based fantasy adventure.")
    print("Create a character to begin.")
    print()
    player = create_character()
    citygate = citygate.CityGate("city", 1, 2)
    player.location = citygate
    launch()
#   print(player.name)
#   print(player.race)
#   print(player.sex)
#   print(player.inventory)
#   print(player.get_stats())

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
    return player.Player(name, race, sex)

def launch():
    print(player.location.title)
    print(player.location.current_desc)
    player.location.first_visit = False
    action = input(" >> ")
    while action != q:
        action = input(" >> ")
            

    
main()

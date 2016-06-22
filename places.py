class Location():
    def __init__(self, x, y):
        self.x = x
        self.y = y    

class City(Location):
    def __init__(self, x, y, area, title, current_desc):
        Location.__init__(self, x, y)
        self.area = area
        self.first_vist = True
        self.title = title
        self.current_desc = current_desc

fountain = City(1, 1, 'C', 'FOUNTAIN', 'A giant fountain, dedicated to the Syfrian Royal Family, sits in front of you.  A number of the nicer shops in Syfri surround the fountain.')

city_gate = City(1, 2, 'C', 'CITY GATE', 'The city gate is guarded on the ground by four members of the royal guard, two on each side of the gate.  Their red uniforms are clean and impressive.  A large statue of a man on a horse sits twenty feet from the gate.  People bustle about, while the guards keep a sharp eye on them.  Up above the gate several members of the royal guard are visible on the wall.')

shanty_town = City(1, 3, 'C', 'SHANTY TOWN', 'You find yourself in the undesirable neighborhood of Syfri.  Hovels, makeshift homes, and garbage are everywhere.')

west_res_area = City(2, 1, 'C', 'WESTERN RESIDENTIAL DISTRICT', 'You\'re in the western residential district, the nicest part of Syfri.  The wealthiest, well protected, homes are located here. ')

city_center = City(2, 2, 'C', 'CITY CENTER', 'You\'re standing in the center of Syfri.  An open air market surrounding a statue of the first king of Syfri, Inolias marks the very center of town.  Surrounding the market is a variety of shops and other commercial buildings.')

field = City(2, 3, 'C', 'FIELD', 'You stand in an underdeveloped part of Syfri, what is essentially a large field.  There is a large structure that is as decripit as it is old--and it is very old.')

east_res_area = City(3, 1, 'C', 'EASTERN RESIDENTIAL DISTRICT', 'The eastern residential district is the more modest section of Syfri.  This is where the average Syfrian lives.')

castle = City(3, 2, 'C', 'CASTLE', 'You stand before the castle gates.  The Royal Guard has a large presence, and there are a number of uniformed soldiers who keep glancing your way.')

tavern_area = City(3, 3, 'C', 'TAVERN DISTRICT', 'You find yourself in the tavern district of Syfri.  There are a number of inns and taverns before you.  Nearest you is The Livid Dragon Inn and The Tangled Web Tavern.')

city_locations = {'C_1_1': fountain, 'C_1_2': city_gate, 'C_1_3': shanty_town,
                  'C_2_1': west_res_area, 'C_2_2': city_center, 'C_2_3': field,
                  'C_3_1': east_res_area, 'C_3_2': castle, 'C_3_3': tavern_area}
        


                            
	
#	    if self.x == 1:
#            if self.y == 1:
#                self.name = 'Fountain'
#                self.description = 'DESCRIPTION OF THE AREA'
#                action = raw_input("> ")

    

                

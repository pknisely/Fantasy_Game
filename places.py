class Location():
    def __init__(self, x, y):
        self.area = area
        self.x = x
        self.y = y    

class City(Location):
    def __init__(self, x, y, area):
		Location.__init__(self, x, y)
		self.area = 'city'
	
	
#	    if self.x == 1:
#            if self.y == 1:
#                self.name = 'Fountain'
#                self.description = 'DESCRIPTION OF THE AREA'
#                action = raw_input("> ")

class CityGate(City):

    def __init__(self, area, x, y):
        self.area = area
        self.x = x
        self.y = y    
        self.title = "CITY GATE"
        self.first_visit = True

        if self.first_visit == True and player.race in (1, 2, 3, 4):
            self.current_desc = "The city gate is guarded on the ground by four members of the royal guard, two on each side of the gate.  Their red uniforms are clean and impressive.  A large statue of a man on a horse sits twenty feet from the gate.  People bustle about, while the guards keep a sharp eye on them.  Up above the gate several members of the royal guard are visible on the wall."

        if self.first_visit == False:
            self.current_desc = "The city gate is guarded on the ground by four members of the royal guard, two on each side of the gate.  Their red uniforms are clean and impressive.  A large statue of a man on a horse sits twenty feet from the gate.  People bustle about, while the guards keep a sharp eye on them.  Up above the gate several members of the royal guard are visible on the wall."
       
    

                

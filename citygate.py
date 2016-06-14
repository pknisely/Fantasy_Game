import location

class CityGate():

    def __init__(self, area, x, y):
        self.area = area
        self.x = x
        self.y = y    
        self.title = "CITY GATE"
        self.first_visit = True

        if self.first_visit == True:
            self.current_desc = "The city gate is guarded on the ground by four members of the royal guard, two on each side of the gate.  Their red uniforms are clean and impressive.  A large statue of a man on a horse sits twenty feet from the gate.  People bustle about, while the guards keep a sharp eye on them.  Up above the gate several members of the royal guard are visible on the wall."

        if self.first_visit == False:
            self.current_desc = "The city gate is guarded on the ground by four members of the royal guard, two on each side of the gate.  Their red uniforms are clean and impressive.  A large statue of a man on a horse sits twenty feet from the gate.  People bustle about, while the guards keep a sharp eye on them.  Up above the gate several members of the royal guard are visible on the wall."
       
    

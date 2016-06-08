class City(Location):
    def __init__(self, area, x, y):
        self.area = 'city'
        self.x = x
        self.y = y

        if x == 1:
            if y == 1:
                self.name = 'Fountain'
                self.description = 'DESCRIPTION OF THE AREA'
                action = raw_input("> ")

                

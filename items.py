
class Item():
	def __init__(self, name):
		self.name = name

class Weapon(Item):
    def __init__(self, name, damage, weaponRange):
        Item.__init__(self, name)
        self.damage = damage
        self.weaponRange = weaponRange
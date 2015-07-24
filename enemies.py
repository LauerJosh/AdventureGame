class Enemy():
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
		
	def is_alive(self):
		return self.hp>0
		
	def stats(self):
		return "Enemy is a {} with {} HP and does {} damage.".format(self.name, self.hp, self.damage)
		
class Bandit(Enemy):
	def __init__(self):
		super().__init__(name = "Bandit", hp=10, damage=2)
		
class Ghoul(Enemy):
	def __init__(self):
		super().__init__(name="Ghoul", hp=30, damage=15)

		
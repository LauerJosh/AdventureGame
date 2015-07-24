import unittest
import items
import enemies
import tiles
import world
import player
import actions
import game
import MaxUnitTestPy

class testItems(unittest.TestCase):

	def testItem(self):
		self.assertEqual(items.Item('Sword', 'Sword', 20).__str__(), "Sword\n\=====\nSword\nValue: 20\n")
		#MaxUnitTestPy.testEqual(items.Item('Sword', 'Sword', 20).__str__(), "Sword\n\=====\nSword\nValue: 20\n")
	
	def testGold(self):
		self.assertEqual(items.Gold(20).__str__(), "Gold\n\=====\nA round coin with 20 stamped on the front.\nValue: 20\n")
	
	def testWeapon(self):
		self.assertEqual(items.Weapon('Sword', 'Sword', 20, 10).__str__(), "Sword\n=====\nSword\nValue: 20\nDamage: 10")
		
	def testRock(self):
		self.assertEqual(items.Rock().__str__(), "Rock\n=====\nA plain rock. Good for bludgeoning.\nValue: 0\nDamage: 5")
		
	def testDagger(self):
		self.assertEqual(items.Dagger().__str__(), "Dagger\n=====\nA sharp-looking dagger.\nValue: 10\nDamage: 10")
		
class testEnemies(unittest.TestCase):
	def testEnemy(self):
		self.assertEqual(enemies.Enemy("Wolf", 10, 5).stats(),"Enemy is a Wolf with 10 HP and does 5 damage.")
		
	def testBandit(self):
		self.assertEqual(enemies.Bandit().stats(),"Enemy is a Bandit with 10 HP and does 2 damage.")
		
	def testGhoul(self):
		self.assertEqual(enemies.Ghoul().stats(), "Enemy is a Ghoul with 30 HP and does 15 damage.")


	
if __name__ == '__main__':
    unittest.main()
import random

class ability:
	def __init__(self, name, max_damage):
		self.name = name
		self.max_damage = max_damage

	def attack(self):
		'''returns a random damage value between 0 and max_damage'''
		return random.randint(0, self.max_damage)

if __name__ == "__main__":
	fireball = ability("Fireball", 50)
	print(fireball.attack())
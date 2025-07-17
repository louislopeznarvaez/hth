#lab6.py louis lopez narvaez
import random
from  ability import ability
from  armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities=[]
        self.armors=[]


    def battle(self, opponent):
     '''Fight another hero and randomly declare a winner'''
     
     winner= random.choice([self.name, opponent])
     print(f"the winner is {winner}!")

    def add_ability(self, ability):
     self.abilities.append(ability)

    def sum_of_attacks(self):
        total_damage = 0

        for ability in self.abilities:
          total_damage += ability.attack()

        return total_damage
    
    def add_armor(self, armor):
        self.armors.append(armor)
    
    def defend(self):
        total_block =0
        for armor in self.armors:
            total_block += armor.block()
        return total_block




if __name__ == "__main__":
    my_hero = Hero("superman", 200)
    print(my_hero.name)            
    print(my_hero.current_health)  

    my_hero1 = Hero("zombie flash", 200)
    print(my_hero1.name)            
    print(my_hero1.current_health)  

    my_hero.battle("batman")
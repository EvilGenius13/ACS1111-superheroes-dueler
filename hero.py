import random
from ability import Ability
from armour import Armour
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armours = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    def fight(self, opponent):
        if (len(self.abilities) == 0) and (len(opponent.abilities) == 0):
            print("Both heroes will go home to their families tonight.")
        else: 
            while True:
                atk_damage = self.attack()
                atk_opponent_damage = opponent.attack()
                self.take_damage(atk_opponent_damage)
                #print(self.current_health)
                #print(self.isalive())
                opponent.take_damage(atk_damage)
                #print(opponent.current_health)
                #print(opponent.isalive())
                #print('--------------------')
                if self.isalive() == False and opponent.isalive() == False:
                    print(f"Neither hero made it through the battle.")
                    self.add_kill(), self.add_death()
                    opponent.add_kill(), opponent.add_death()
                    break
                elif self.isalive() == False and opponent.isalive() == True:
                    print(f"Sadly, our hero {self.name} was defeated by {opponent.name}")
                    self.add_death(), opponent.add_kill()
                    break
                elif opponent.isalive() == False and self.isalive() == True:
                    print(f"Our hero {self.name} defeated {opponent.name}")
                    self.add_kill(), opponent.add_death()
                    break
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armour(self, armour):
        self.armours.append(armour)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_block = 0
        for armour in self.armours:
            total_block += armour.block()
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        self.current_health -= damage - defense
    
    def isalive(self):
        if self.current_health <= 0:
            return False
        else:
            return True
    
    def add_kill(self):
        self.kills += 1
    
    def add_death(self):
        self.deaths += 1
         

if __name__ == "__main__":
    hero1 = Hero('Jaina Proudmoore')
    hero2 = Hero("Gul'dan")
    ability1 = Ability('Frostbolt', 5)
    ability2 = Ability('Incinerate', 5)
    # ability3 = Ability('Dagger', 15)
    # ability4 = Ability('Throwing Dagger', 7)
    hero1.add_ability(ability1)
    # hero1.add_ability(ability3)
    hero2.add_ability(ability2)
    # hero2.add_ability(ability4)
    hero1.fight(hero2)

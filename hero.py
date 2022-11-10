import random
from ability import Ability
from armour import Armour

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armours = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        roll = random.randint(0, 1)
        if roll == 1:
            print(f"{self.name} defeats {opponent.name}")
        else: 
            print(f"{opponent.name} defeats {self.name}")

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armour(self, armour):
        self.armours.append(armour)
    
    def defend(self):
        total_block = 0
        for armour in self.armours:
            total_block += armour.block()
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        self.current_health -= damage - defense
    
    def isalive(self, opponent):
        if len(self.abilities == 0) or len(opponent.abilites == 0):
            print(f"It's a draw.")
        else: 
            while self.current_health >0 or opponent.current_health > 0:
                total_damage = self.attack()
                opponent.take_damage(total_damage)

                if opponent.isalive() == True:
                    total_damage = opponent.attack()
                    self.take_damage(total_damage)
                    if self.isalive() == True:
                        total_damage = total_damage = self.attack()
                        opponent.take_damage(total_damage)
                    else:
                        return print(f"{opponent.name} won the round!")
                elif opponent.isalive() == False:
                    return print(f"{self.name} won the round!")
         

if __name__ == "__main__":
    hero1 = Hero('Jaina Proudmoore')
    hero2 = Hero("Gul'dan")
    # ability1 = Ability('Dagger', 5)
    # ability2 = Ability('Sword', 10)
    # ability3 = Ability('Dagger', 15)
    # ability4 = Ability('Throwing Dagger', 7)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability3)
    # hero2.add_ability(ability2)
    # hero2.add_ability(ability4)
    hero1.fight(hero2)
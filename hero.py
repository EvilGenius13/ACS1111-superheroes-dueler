import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    
    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        roll = random.randint(0, 1)
        if roll == 1:
            print(f"{self.name} defeats {opponent.name}")
        else: 
            print(f"{opponent.name} defeats {self.name}")





if __name__ == "__main__":
    hero = Hero("Superman", 200)
    villain = Hero("Joker", 200)
    hero.name
    hero.fight(villain)
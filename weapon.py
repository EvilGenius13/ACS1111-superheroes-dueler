from ability import Ability
import random

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)
    
    def attack(self):
        random_value = random.randint(self.max_damage // 2, self.max_damage)
        return random_value    
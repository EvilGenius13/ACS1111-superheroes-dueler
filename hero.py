import random

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
    my_hero = Hero("Grace Hopper", 200)
    opponent = Hero("Bad Dude", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    my_hero.fight(opponent)

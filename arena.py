from ability import Ability
from weapon import Weapon
from armour import Armour
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one: None
        self.team_two: None
    
    def create_ability(self):
        name = input("What is the ability name?: ")
        max_damage = int(input("What is the max damage of the ability?: "))
        return Ability(name, max_damage)
    
    def create_weapon(self):
        name = input("What is the weapon name?: ")
        max_damage = int(input("What is the max damage of the weapon?: "))
        return Weapon(name, max_damage)
    
    def create_armour(self):
        name = input("What is your armour name?: ")
        max_defense = int(input("What is the max defense of the armour?: "))
        return Armour(name, max_defense)
    
    def create_hero(self):
        hero_name = input("What is your hero name?: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armour = self.create_armour()
                hero.add_armour(armour)
        return hero
    
    def build_team_one(self):
        team_name = input("What's your team name?: ")
        self.team_one = Team(team_name)
        num_of_members = int(input("How many members should be on Team One?:\n"))
        for i in range(num_of_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
    
    def build_team_two(self):
        team_name = input("What's your team name?: ")
        self.team_two = Team(team_name)
        num_of_members = int(input("How many members should be on Team Two?:\n"))
        for i in range(num_of_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
    
    def team_battle(self):
        self.team_one.attack(self.team_two)

    def kd_ratio(self, team):
        team_kills = 0
        team_deaths = 0
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
            kd_total = team_kills / team_deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f"{team.name} average K/D was: {kd_total}")
    
    def survivors(self, team):
        survivors = 0
        for hero in team.heroes:
            if hero.deaths == 0:
                survivors += 1
                print(f"{hero.name} from {team.name} survived the battle.")
        return survivors

    def show_stats(self):
        survivors_team_one = self.survivors(self.team_one)
        survivors_team_two = self.survivors(self.team_two)

        if survivors_team_one > survivors_team_two:
            print(f"Congratulations {self.team_one.name}, you won!")
        elif survivors_team_two > survivors_team_one:
            print(f"Congratulations {self.team_two.name}, you won!")
        
        print(f"-----------------")
        print(f"{self.team_one.name} Final Stats:")
        self.team_one.stats()
        print(f"-----------------")
        print(f"{self.team_two.name} Final Stats:")
        self.team_two.stats()
        print(f"-----------------")

        self.kd_ratio(self.team_one), self.kd_ratio(self.team_two)
        print(f"-----------------")

if __name__ == "__main__":
    game_is_running = True
    #Build Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()
    
    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == 'n':
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

import random

class Armour:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value


if __name__ == "__main__":
    armour = Armour("Wooden Shield", 10)
    print(armour.name)
    print(armour.block())
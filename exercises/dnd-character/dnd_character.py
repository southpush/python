import random


def modifier(num):
    return int((num - 10) // 2)


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        results = [random.randint(1, 6) for i in range(4)]
        return sum(results) - results.pop(random.randint(0, 3))

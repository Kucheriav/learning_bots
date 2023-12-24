import random

class Unit:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.text_coord = f'{self.pos_x}:{self.pos_y}'

    def set_position(self, new_x, new_y):
        if new_x > 0 and new_y > 0:
            self.pos_x = new_x
            self.pos_y = new_y

    def get_position(self):
        self.text_coord = f'{self.pos_x}:{self.pos_y}'
        return self.text_coord


class Warrior(Unit):
    def __init__(self, pos_x, pos_y, name):
        super().__init__(pos_x, pos_y)
        self.name = name
        self.strength = random.randint(3,5)
        self.health = random.randint(17, 20)
        self.speed = random.randint(1, 3)

    def greeting(self):
        print(f"Привет, я {self.name} с {self.health} кол-во здоровья и {self.strength} силой")

    def move(self):
        self.set_position(self.pos_x + self.speed, self.pos_y + self.speed)

    def attack(self, enemy):
        if not isinstance(enemy, Warrior):
            print('Таких бить нельзя')
            return
        enemy.health -= self.strength


def print_statistics(*units):
    for unit in units:
        print(f"Воин {unit.name}. Здоровья {unit.health}. Атака {unit.strength}")

class Observer:
    def init_game(self):
        pass

    def check_victory(self):
        pass

    def comment(self):
        pass

ork1 = Warrior(1, 1,"Gork")
ork1.greeting()
ork2 = Warrior(1, 1,"Mork")
ork2.greeting()
while True:
        print_statistics(ork1, ork2)
        ork1.attack(ork2)
        ork2.attack(ork1)
        if ork1.health < 0 or ork2.health < 0:
            break
        print()
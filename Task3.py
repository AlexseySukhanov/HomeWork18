from datetime import datetime

class Marine:
    def __init__(self, division, health, armor):
        self.speed = 50
        self.hit = 10
        self.division = division
        self.health = health
        self.armor = armor

    def __setattr__(self, key, value):
        with open('change.log','a') as file:
            file.write(f'{key} setted to {value} at {datetime.now()}\n')
            file.close()

        self.__dict__[key] = value

    def __str__(self):
        return f'Devision: {self.division}\n' \
               f'Health: {self.health}\n' \
               f'Armor: {self.armor}\n' \
               f'Speed: {self.speed}\n' \
               f'Hit: {self.hit}\n'

unit1 = Marine('Snow', 100, 90)
unit1.hit = 20
unit1.hit = 50
unit1.speed = 10000
unit1.armor = 15
print(unit1)
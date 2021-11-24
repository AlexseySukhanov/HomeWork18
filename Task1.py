class Marine:
    def __init__(self, division, health, armor):
        self.division = division
        self.health = health
        self.armor = armor

    def __setattr__(self, key, value):
        match key:
            case 'speed' :
                self.__dict__['speed'] = 50
            case 'hit' :
                self.__dict__['hit'] = 10
            case _:
                self.__dict__[key] = value

    def __str__(self):
        return f'Devision: {self.division}\n' \
               f'Health: {self.health}\n' \
               f'Armor: {self.armor}\n'\
               f'Speed: {self.speed}\n'\
               f'Hit: {self.hit}\n'



unit1 = Marine('Snow',100,90)
unit1.hit = 20
unit1.hit = 50
unit1.speed = 10000
unit1.armor = 15
print(unit1)
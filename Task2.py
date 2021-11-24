class Marine:
    def __init__(self, health, armor):
        self.speed = 50
        self.hit = 10
        self.health = health
        self.armor = armor

    def __setattr__(self, key, value):
        if not isinstance(value, int):
            raise TypeError()

        self.__dict__[key] = value


    def __str__(self):
        return f'Health: {self.health}\n' \
               f'Armor: {self.armor}\n'\
               f'Speed: {self.speed}\n'\
               f'Hit: {self.hit}\n'



unit1 = Marine(100,90)
unit1.hit = 20
unit1.hit = 50
unit1.speed = 10000
unit1.armor = "hard"
print(unit1)
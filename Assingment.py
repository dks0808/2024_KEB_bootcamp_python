# Pokemon game assignment
import random

class W_attackMixin:
    def water(self):
        return f"{self.__name}이(가) 하늘을 훨훨 날아갑니다~"

class F_attackMixin:
    def flame(self):
        return f"{self.__name}이(가) 수영을 합니다."

class E_attackMixin:
    def electric(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Plant_attackMixin: # never function in Pikachu
    def plant(self):
        return f"{self.__name}이(가) 수영을 합니다."

class FlyMixin:
    def Fly(self):
        return f'fly'

class Pokemon:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def mana_point(self):
        mp = 100
        return mp

    def heart_point(self):
        hp = 100
        return hp

    def attack(self):
        print('defalt attack')

    def evolution_Lv(self):
        ev = 1
        return ev


    #name = property(get_name, set_name)


class Charmander(Pokemon,F_attackMixin):
    def mana_point(self):
        mp = 100
        return mp

    def heart_point(self):
        hp = 100
        return hp

    def attack(self):
        print('defalt attack')

    def type(self):
        t = 'Fire'
        return t

class Bulbasaur(Pokemon,Plant_attackMixin):
    def mana_point(self):
        mp = 100
        return mp

    def heart_point(self):
        hp = 100
        return hp

    def attack(self):
        print('defalt attack')
    def type(self):
        t = 'Plant'
        return t

class Gyarados(Pokemon,W_attackMixin):
    def mana_point(self):
        mp = 100
        return mp

    def heart_point(self):
        hp = 100
        return hp

    def attack(self):
        print('defalt attack')
    def type(self):
        t = 'Fly','Water'
        return t

class Pikachu(Pokemon,E_attackMixin):
    def mana_point(self):
        mp = 100
        return mp

    def heart_point(self):
        hp = 100
        return hp

    def attack(self):
        print('defalt attack')
    def type(self):
        t = 'Electric'
        return t

class Squirtle(Pokemon,W_attackMixin):
    def mana_point(self):
        mp = 100
        return mp

    def heart_point(self):
        hp = 100
        return hp

    def attack(self):
        print('defalt attack')
    def type(self):
        t = 'Water'
        return t


class Charmander_2(Pokemon, F_attackMixin,Charmander):
    def mana_point(self):
        mp = 250
        return mp

    def heart_point(self):
        hp = 150
        return hp


class Bulbasaur_2(Pokemon, Plant_attackMixin,Bulbasaur):
    def mana_point(self):
        mp = 100
        return mp

    def heart_point(self):
        hp = 100
        return hp

class Gyarados_2(Pokemon, W_attackMixin, Gyarados):
    def mana_point(self):
        mp = 120
        return mp

    def heart_point(self):
        hp = 300
        return hp


class Pikachu_2(Pokemon, E_attackMixin, Pikachu):
    def mana_point(self):
        mp = 200
        return mp

    def heart_point(self):
        hp = 150
        return hp


class Squirtle_2(Pokemon, W_attackMixin, Squirtle):
    def mana_point(self):
        mp = 150
        return mp

    def heart_point(self):
        hp = 200
        return hp


# naming
p1 = Pikachu("Pikachu")
c1 = Charmander("Charmander")
b1 = Bulbasaur("Bulbasaur")
g1 = Gyarados("Gyarados")
s1 = Squirtle("Squirtle")

p2 = Pikachu_2("Pikachu2")
c2 = Charmander_2("Charmander2")
b2 = Bulbasaur_2("Bulbasaur2")
g2 = Gyarados_2("Gyarados2")
s2 = Squirtle_2("Squirtle2")

# the attribute
p1a = [p1.name, p1.heart_point(), p1.mana_point(), p1.type() ]
c1a = [c1.name, c1.heart_point(), c1.mana_point(), c1.type() ]
b1a = [b1.name, b1.heart_point(), b1.mana_point(), b1.type() ]
g1a = [g1.name, g1.heart_point(), g1.mana_point(), g1.type() ]
s1a = [s1.name, s1.heart_point(), s1.mana_point(), s1.type() ]

p2a = [p2.name, p1.heart_point(), p1.mana_point(), p1.type() ]
c2a = [c2.name, c2.heart_point(), c2.mana_point(), c2.type() ]
b2a = [b2.name, b2.heart_point(), b2.mana_point(), b2.type() ]
g2a = [g2.name, g2.heart_point(), g2.mana_point(), g2.type() ]
s2a = [s2.name, s2.heart_point(), s2.mana_point(), s2.type() ]

menu = input(f"Choose your own pokemon. \n 1) Pikachu, 2) Charmander, 3) Bulbasaur, 4)Gyarados, 5)Squirtle, 6) Quit 'press 6 or q' : ")
options = '12345q'
while menu in options:
    if menu ==1:
        print('You got the pikachu!')

        print(f'Pikachu is {p1a}')
        break


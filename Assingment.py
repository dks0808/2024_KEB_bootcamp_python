# Pokemon game assignment
import random

# attack class control this for dick
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


# basic evolution attribute class with Top Class
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



# basic evolution level class
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

# advance evolutions class
class Mega_Charizard(Charmander, F_attackMixin):
    def mana_point(self):
        mp = 250
        return mp

    def heart_point(self):
        hp = 150
        return hp
class Ivysaur(Bulbasaur, Plant_attackMixin):
    def mana_point(self):
        mp = 100
        return mp

    def heart_point(self):
        hp = 100
        return hp
class Mega_Gyarados(Gyarados, W_attackMixin):
    def mana_point(self):
        mp = 120
        return mp

    def heart_point(self):
        hp = 300
        return hp
class Raichu(Pikachu, E_attackMixin):
    def mana_point(self):
        mp = 200
        return mp

    def heart_point(self):
        hp = 150
        return hp
class Wartortle(Squirtle, W_attackMixin):
    def mana_point(self):
        mp = 150
        return mp

    def heart_point(self):
        hp = 200
        return hp


# basic evolution level class naming partition
p1 = Pikachu("Pikachu")
c1 = Charmander("Charmander")
b1 = Bulbasaur("Bulbasaur")
g1 = Gyarados("Gyarados")
s1 = Squirtle("Squirtle")

# advance evolutions class naming partition
p2 = Raichu("Raichu")
c2 = Mega_Charizard("Mega_Charizard")
b2 = Ivysaur("Ivysaur")
g2 = Mega_Gyarados("Mega_Gyarados")
s2 = Wartortle("Wartortle")

def bea(number): # basic evolution attributes dictionary
    p1a = {"Name": p1.name, 'Hp': p1.heart_point(), 'Mp' : p1.mana_point(), 'Type': p1.type()}
    c1a = {"Name": c1.name, 'Hp': c1.heart_point(), 'Mp' : c1.mana_point(), 'Type': c1.type()}
    b1a = {"Name": b1.name, 'Hp': b1.heart_point(), 'Mp' : b1.mana_point(), 'Type': b1.type()}
    g1a = {"Name": g1.name, 'Hp': g1.heart_point(), 'Mp' : g1.mana_point(), 'Type': g1.type()}
    s1a = {"Name": s1.name, 'Hp': s1.heart_point(), 'Mp' : s1.mana_point(), 'Type': s1.type()}
    if number == 1:
        return p1a
    elif number == 2:
        return c1a
    elif number == 3:
        return b1a
    elif number == 4:
        return g1a
    elif number == 5:
        return s1a


def aea(number): # advance evolution attributes dictionary
    p2a = {"Name": p2.name, 'Hp': p2.heart_point(), 'Mp' : p2.mana_point(), 'Type': p2.type()}
    c2a = {"Name": c2.name, 'Hp': c2.heart_point(), 'Mp' : c2.mana_point(), 'Type': c2.type()}
    b2a = {"Name": b2.name, 'Hp': b2.heart_point(), 'Mp' : b2.mana_point(), 'Type': b2.type()}
    g2a = {"Name": g2.name, 'Hp': g2.heart_point(), 'Mp' : g2.mana_point(), 'Type': g2.type()}
    s2a = {"Name": s2.name, 'Hp': s2.heart_point(), 'Mp' : s2.mana_point(), 'Type': s2.type()}
    if number == 1:
        return p2a
    elif number == 2:
        return c2a
    elif number == 3:
        return b2a
    elif number == 4:
        return g2a
    elif number == 5:
        return s2a


# basic evolution attributes ver list
# p1a = [p1.name, p1.heart_point(), p1.mana_point(), p1.type()]
# c1a = [c1.name, c1.heart_point(), c1.mana_point(), c1.type()]
# b1a = [b1.name, b1.heart_point(), b1.mana_point(), b1.type()]
# g1a = [g1.name, g1.heart_point(), g1.mana_point(), g1.type()]
# s1a = [s1.name, s1.heart_point(), s1.mana_point(), s1.type()]

# # advance evolution attributes ver list
# p2a = [p2.name, p2.heart_point(), p2.mana_point(), p2.type()]
# c2a = [c2.name, c2.heart_point(), c2.mana_point(), c2.type()]
# b2a = [b2.name, b2.heart_point(), b2.mana_point(), b2.type()]
# g2a = [g2.name, g2.heart_point(), g2.mana_point(), g2.type()]
# s2a = [s2.name, s2.heart_point(), s2.mana_point(), s2.type()]

start = input('If You wanna play Pokemon game, Press "p". \n press any keys if you wanna quit this. : ')
operate(start)
# operating function
def operate(key):
    """
    function of program operating. If this function be called, it will call select function.
    :param key: str
    :return: str
    """
    if key == 'p' or 'P':
        menu = input(f"Choose your own pokemon. \n 1) Pikachu, 2) Charmander, 3) Bulbasaur, 4)Gyarados, 5)Squirtle, 6) Quit 'press 6 or q' : ")
        select(menu)

    else:
        print("good bye")

# Pokemon select
def select(c):
    """
    function of selecting character
    :param c:
    :return:
    """
    options = '12345q'
    while c in options:
        if c =='1':
            a = f'You got the {p1.name}'
            b = f'{p1.name} is {bea(1)}'
            print(a,b)
            break

        elif c =='2':
            a = f'You got the {c1.name}'
            b = f'{c1.name} is {bea(2)}'
            print(a,b)
            break

        elif c =='3':
            a = f'You got the {b1.name}'
            b = f'{b1.name} is {bea(3)}'
            print(a,b)
            break

        elif c =='4':
            a = f'You got the {g1.name}'
            b = f'{g1.name} is {bea(4)}'
            print(a,b)
            break

        elif c =='5':
            a = f'You got the {s1.name}'
            b = f'{s1.name} is {bea(5)}'
            print(a,b)
            break

        else:
            print(f'')


class S_attackMixin:
    def water(self):
        return f"{self.__name}이(가) 하늘을 훨훨 날아갑니다~"

class C_attackMixin:
    def flame(self):
        return f"{self.__name}이(가) 수영을 합니다."

class P_attackMixin:
    def electric(self):
        return f"{self.__name}이(가) 수영을 합니다."

class B_attackMixin:
    def plant(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def mana_point:
        mp = 100
        return mp
    def heart_point:
        hp = 100
        return hp
    def attack(self):
        print("")

    def evolution_Lv:
        ev = 1
        return ev


    #name = property(get_name, set_name)


class Charmander(Pokemon):
    pass

class Bulbasaur(Pokemon):
    pass
class Gyarados(Pokemon):
    pass




#mixin
class Flymixin:
    def fly(self):
        return f"{self.__name}이(가) 하늘을 난다."

class Swimmingmixin:
    def swim(self):
        return f'{self.__name}이(가) 헤엄을 칩니다.'
class Poketmon:
    def __init__(self, name):
        self.__name = name
    def attack(self):
        print('attack')
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        self.__name = new_name

    # name = property(get_name, set_name)
class Charizard(Poketmon,Flymixin):
    pass

class Gyrados(Poketmon,Swimmingmixin):
    pass

c1 = Charizard('리자몽')
g1 = Gyrados('갸라도스')
#
# print(p1.fly())
# print(p2.swim())
# # 해당 코드는 다중 상속을 사용한 mixin
# #다중상속 쓸 때는 mro에 유의 하여한다.
# p1.attack()
# Charizard.attack(p1) # 원래 객체 뒤에 메소드를 사용하지만 클래스 직접 사용하려면 괄호에 객체를 넣어줘야함
#
# print(p1. name)
# p1.name = '리자스몽'# direct access
# print(p1.name)
#
# p1.set_name('리자몽')
# print(p1.name)

# property 사용
print(g1.name)
g1.name = "야도란"
print(g1.name)
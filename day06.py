#mixin
class Flymixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 난다."

class Swimmingmixin:
    def swim(self):
        return f'{self.name}이(가) 헤엄을 칩니다.'
class Poketmon:
    def __init__(self,name):
        self.name = name

class Charizard(Poketmon,Flymixin):
    pass

class Gyrados(Poketmon,Swimmingmixin):
    pass

p1 = Charizard('리자몽')
p2 = Gyrados('갸라도스')

print(p1.fly())
print(p2.swim())
# 해당 코드는 다중 상속을 사용한 mixin
#다중상속 쓸 때는 mro에 유의 하여한다.
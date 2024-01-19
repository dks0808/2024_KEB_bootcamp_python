class Poketmon:
    def __init__(self,name):
        self.name = name

    def attack(self,target):
        print(f'{self}이(가) {target.name}을(를) 공격!' )

    pass
class Pikachu(Poketmon): # 부모 클래스의 이름을 괄호에 입력 is-a 관계
    def attack(self,target):
        print(f'{self}이(가) {target.name}을(를) {self.type} 공격!' )

    def __init__(self,name, type):
        self.type = type
        super().__init__(name)
    def electronic_info(self):
        print('일렉트로 공격을 합니다.')

    pass

class Agumon(Poketmon):
    def attack(self,target):
        print(f'{self}이(가) {target.name}을(를) {self.type}공격!' )

    def __init__(self,name, type):
        self.type = type
        super().__init__(name)
    pass

p1 = Pikachu('피카츄', '전기')
print(p1.name)

a1 = Agumon('아구몬', '화염')
print(a1.name)
p1.attack(a1)



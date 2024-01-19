class Poketmon: #소괄호 사용해도 되고 안해도 됨. 사용하면 올드함.
    def __init__(self, name): #self 는 defalt,자동으로 들어가는 매개 변수이다. init = initialize init은 각 개체마다 태어날 때마다 딱 한번만 돌아감
        self.name = name
        print(f"{name} 포켓몬 생성")
    pass
    def attck(self, target):
        print(f"{self.name}이(가) {target.name}을 공격")
# name 필드를 가지고 할당한다.
# self 는 해당 기능을 실행하고 있는 주체인 객체를 가르킨다.
charizard = Poketmon('리자몽')
pikachu = Poketmon('피카츄')
squirtle = Poketmon('꼬북이')

charizard.attck(squirtle)
print(pikachu.name)
print(squirtle.name)
print(charizard.name)


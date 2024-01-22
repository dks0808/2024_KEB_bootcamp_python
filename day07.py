class Pikachu:
    def __init__(self, name, hp, fly):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.fly_behavior = fly  # aggregation
        self.fly_behavior = NoFly()  # composition


nofly = NoFly()
p1 = Pikachu("피카츄", 35, nofly)
p1 = Pikachu("피카츄", 35)
print(p1.fly_behavior.fly())
#입력값은 100과 50
numbers = input("Enter the number1, number2.").split()
n1 =int(numbers[0])
n2 =int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2+1):
    is_prime = True # is_prime 을 반복 마다 True 로 주어야함.

    if number < 2:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime =False
                break
        if is_prime: print(number, end=' ')
# number 같은 것은 for 문 안에서만 작동하기 때문에 선언을 따로 하지 않아도 됨.



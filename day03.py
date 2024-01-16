#입력값은 100과 50

numbers = input("Enter the number1, number2.").split()
n1 =int(numbers[0])
n2 =int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1,n2+1):
    is_prime = True # is_prime 을 반복 마다 True 로 주어야함.

    if number < 2:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime =False
                break
        if is_prime: print(number, end=' ')

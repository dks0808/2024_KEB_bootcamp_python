def isprime(n) -> bool: # boolean type hint
    """
    매개변수로 넘겨 받은 수의 소수 여부를 불린 boolean 으로 return
    :param n: 판정할 매개변수
    :return: 소수면 True, 아니면 False
    """
    if n < 2:
        return False
    else:
        i =2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

numbers = input("Enter the number1, number2.").split()

n1 =int(numbers[0])
n2 =int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2+1):
    if isprime(number):
        print(number, end=' ')
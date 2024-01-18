#과제 1
# 5 Options to operate prime with function
def isprime(n) -> bool: # boolean type hint
    """
    매개변수로 넘겨 받은 수의 소수 여부를 불린 boolean 으로 return
    :param n: 판정할 매개변수
    :return: 소수면 True, 아니면 False
    """
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

while True:
    Options = input("""1) Fahrenheit to Celsius, 2) Celsius to Fahrenheit, 
    3) Prime Number scaner, 4) Scaner between two number 5) Quit : """)

    if Options == '1':
        Fahrenheit = float(input("Enter the Fahrenheit. : "))
        print(f"{Fahrenheit}F is {(Fahrenheit - 32) * 5 / 9:.4f}C")

    elif Options == '2':
        Celsius = float(input("Enter the Celsius. : "))
        print(f"{Celsius}C is {(Celsius * 9.0 / 5.0) + 32:.4f}F")

    elif Options == '3':
        num = int(input("Enter the number. : "))

        if isprime(num):
            print(f"{num} is prime number.")
        else:
            print(f"{num} is NOT prime number.")

    elif Options == '4':
        n1, n2 = map(int, input("Enter the number1 & number2. : ").split())
        # numbers = input("Enter the number1 & number2. : ").split()
        # n1 = int(numbers[0])
        # n2 = int(numbers[1])
        n1, n2 = min(n1, n2), max(n1,n2)

        for number in range(n1, n2 + 1):
            if isprime(number):
                print(number, end=' ') #줄 바꿈 대신에 white space
        print('') # 줄 바꿈 위해 들어감.

    elif Options == '5' or 'q':
        print("Goodbye Have a nice day ^~^")
        break
    else:
        print("Invalid options! Please Enter the number between '1~5' or key 'q' ")
# 문제 1 예외처리, 소수옵션 3,4번의 코드 중복 -> 함수로 해결

#과제 1
import string

while True:
    Options = input("1) Fahrenheit to Celsius, 2) Celsius to Fahrenheit, 3) Prime Number scaner, 4) Scaner between two number 5) Quit : ")
    sel = '12345q'
    if Options in sel:
        if Options == '1':
            Fahrenheit = input("Enter the Fahrenheit. : ")
            while type(Fahrenheit) != float:
                print("Please enter only number.")
                break
            else:
                float(Fahrenheit)
                print(f"{Fahrenheit}F is {(Fahrenheit - 32) * 5 / 9:.4f}C")

        elif Options == '2':
            Celsius = input("Enter the Celsius. :")
            while type(Celsius) != float:
                print("Please enter only number.")
                break
            else:
                float(Celsius)
                print(f"{Celsius}C is {(Celsius * 9.0 / 5.0) + 32:.4f}F")

        elif Options == '3':
            num = int(input("Enter the number. : "))
            is_prime = True
            if num < 2:
                print(f"{num} is NOT prime number.")
            else:
                for i in range(2,num):
                    if num % i == 0:
                        is_prime = False
                        break
                        i += 1
                if is_prime:
                    print(f"{num} is prime number.")
                else:
                    print(f"{num} is NOT prime number.")

        elif Options == '4':
            numbers = input("Enter the number1 & number2. : ").split()
            n1 = int(numbers[0])
            n2 = int(numbers[1])
            if n1 > n2:
                n1, n2 = n2, n1

            for number in range(n1, n2 + 1):
                is_prime = True  # is_prime 을 반복 마다 True 로 주어야함.

                if number < 2:
                    pass
                else:
                    for i in range(2, number):
                        if number % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        print(number, end=' ')
            print('') # 줄 바꿈 위해 들어감.

        elif Options == '5' or 'q':
            print("Goodbye Have a nice day ^~^")
            break
    else:
        print("Please Enter the number between '1~5' or key 'q' ")
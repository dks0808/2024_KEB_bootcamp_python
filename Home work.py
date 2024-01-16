#과제 1
while True:
    Options = input("1) Fahrenheit to Celsius, 2) Celsius to Fahrenheit, 3) Prime number scaner, 4) Scaner between two number 5) Quit : ")
    if Options == '1':
        Fahrenheit = float(input("Enter the Fahrenheit. : "))
        print(f"{Fahrenheit}F is {(Fahrenheit - 32) * 5/9:.4f}C")

    elif Options == '2':
        Celsius = float(input("Enter the Celsius. :"))
        print(f"{Celsius}C is {(Celsius * 9.0/5.0) + 32:.4f}F")

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

        for number in range(n1,n2+1):
            is_prime = True
            if number < 2:
                pass
            else:
                for i in (2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                        i += 1
                if is_prime:
                    print(number, end=' ')

    elif Options == '5':
        print("Goodbye Have a nice day ^~^")
        break

    elif Options == 'q':
        print("Goodbye Have a nice day ^~^")
        break
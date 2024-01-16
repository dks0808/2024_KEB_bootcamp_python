#prime number
number = int(input("Enter the number : "))
is_prime = True
if number < 2:
    print(f'{number} is not prime number')
else:
    i = 2
    while i < number:
        if number % i == 0:
            is_prime =False
            break
        i = i + 1
    if is_prime: #is prime 자체가 불린 형임으로 ==를 붙여줄 필요가 없다.
        print(f'{number} is prime number')
    else:
        print(f'{number} is not prime number')

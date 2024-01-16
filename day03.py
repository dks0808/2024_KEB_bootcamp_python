#prime number
number = int(input("Enter the number : "))
count = 0
i = 2
while i < number:
    if number % i == 0:
        count = count + 1
        break
    i = i + 1
if count == 0:
    print(f'{number} is prime number')
else:
    print(f'{number} is not prime number')

import random

# numbers = list()
# for i in range(5)
#     numbers.append(random.append(1,100))

numbers = [random.randint(1,100) for i in range(10)]
print(numbers)
try:
    pick = int(input(f"Input the number(0~{len(numbers)-1}) : "))
    print(numbers[pick])

except IndexError as err: # as + 변수 이름 하면 시스템에서 만든 문구를 출력
    print(f"out of range: Wrong index number {err}")
except ValueError:
    print("Input only number")
except Exception: #이러한 것은 보험용이기에 맨 밑에 넣어야함
    print("error occurs")

# except 옆에 밑에 창에 뜨는 시스템 에러 이름을 적어주면 됨.
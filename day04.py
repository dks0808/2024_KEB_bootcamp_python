import random

drinks_foods = {"위스키":"초콜렛", "와인":"치즈", "소주":"삼겹살", "고량주":"양꼬치"}
# drink = input(drinks_foods.keys())
del drinks_foods['위스키']
# drinks_foods["사케"]="회"
japan_drinks_foods = {"사케":"회", "위스키":"낙곱새"}
drinks_foods.update(japan_drinks_foods)
drinks_foods_keys =list(drinks_foods)
# 대충 팝에 대한 내용


while True:
    random_drink = random.choice(drinks_foods_keys)  # random 함수의 값은 시퀀스 자료가 아니어도 됨
    menu = input(f"다음 술중에 고르시오.\n 1) {drinks_foods_keys[0]}, 2){drinks_foods_keys[1]}, 3){drinks_foods_keys[2]},4){drinks_foods_keys[3]}, 5){drinks_foods_keys[4]}, 6) 아무거나  6) Quit : ")
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다.')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다.')
    elif menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다.')
    elif menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다.')
    elif menu == '5':
        print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[4]]} 입니다.')
    elif menu == '6':
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다.')

    elif menu == '7' or 'q':
        print(f'quit this program')
        break

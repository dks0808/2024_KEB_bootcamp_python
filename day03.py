university = "Inha\nUniversity!"
#university = r"Inha\nUniversity!"  # raw string
#print(university)

# slicing
# print(university[:4])
# print(university[:-11])
# print(len(university))
# print(university[0:len(university)])
# print(university[:16])
# print(university[::2])

# number1 = input("First number : ")
# number2 = input("Second number : ")
# print(number1 + number2)  # concatenation
# print(number1 * 3)  # duplicate
# print(number1 + 3)  # TypeError: can only concatenate str (not "int") to str
#------------------------
# university = r"Inha \n university!" #\n은한글자
# print(university[:4])
# print(university[:-11]) #[start:end:step]
# print(university[0:len(university)]) #0부터 유니버스티 길이까지
# len(university) #문자열의 경우 문자의 갯수를 출력
# letters = 'abcdefghijklmnopqrsutwvxyz'
# print(len(letters)) #list의 경우 원소갯수 리턴
#
# print(letters[3:25:2])# 4번째 문자부터 26까지 2칸씩 출력
## join list ->str
#
# subjects = ['python', 'C++', 'database']
# subjects_str = " / ".join(subjects)
# print(subjects_str)

# split()# .
#replace(old,new,count)
# course = "2024 KEB Bootcamp" # white space로 작동한다. 리턴 타입이 리스트이다.
# print(course)
# list_course = course.split('B') # 괄호에 어떤 것을 넣어주면 괄호 안에 있는 것을 기준으로 토큰을 나눠줌
# print(list_course)
# print(course.replace('KEB','INHA'))#이경우는 잠시 프린트시에만 임시적으로 바뀐 것임.
#
# course = course.replace('KEB','INHA')
# print(course) #재할당 해주는 것임

course = "KEB 2024# KEB Bootcamp...*!#"
print(course)
course = course.replace('KEB','INHA',1)
print(course)

# strip() 공란 제거 인수에는 제거할 대상 공란 취급할 것 넣는 듯
# lstrip 좌공란 제거
# rstrip 우공란 제거

print(course.strip('!#*.')) #단 양쪽 끝에 있는 것만 제거가 된다.

print(course.find('inha'))


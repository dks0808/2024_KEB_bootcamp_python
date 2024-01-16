subjects ="python C++ database linux"
subject = input("Enter the subject")
# if subjects.find(subject) !=-1:
#     print(f"We can check the subject location is index{subjects.find('C++')}")
# else:
#     print("We can't find that")


#인덱스를 사용한 예외처리
try:
    print(f"We can check the subject location is index{subjects.find(subject)}")
except ValueError:
    print("We can't find that")
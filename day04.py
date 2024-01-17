subjects = ["c++", "5", "Java", "python", "Java", "9"]

# subjects.remove('Java')# 순서대로 지움
# print(subjects)
# del subjects[-1] #특정 값을 지움
# print(subjects)
#
# subjects.pop() # 뒤엣부터 지움
# subjects.pop(1) #앞에서부터 2번째를 지움
#
#

subjects.sort(reverse= True) #원본이 바뀌게 됨.
print(subjects)
copy_subjects = sorted(subjects)
print(copy_subjects)

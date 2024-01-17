t1 = (5)
t2 = (5,)
t3 = (5,7)
t4= 5,7
print(type(t1), type(t2), type(t3), type(t4),)
t6 = "python", "kim"#packing
print(type(t6), t6[1])
subject, prof =t6 # unpacking
print(prof)
print(subject)
# unpacking시 중요한 것은 짝수가 맞는 것이 중요함

# a, b, c = t6 #ValueError: not enough values to unpack (expected 3, got 2)

t7 = ()
print(type(t7)) # t7도 튜플임 T/F 할 때 빈 괄호와 문자열은 F
t8() = tuple()
print(type('im',)) #
print(type(('im',))) #

a = ('yada',) * 3 # 문자열과 같이 3번 반복함
print(a)

t9 = 1,2,3
t10 = 1,2
print(t9<=t10)
print(t9==t10)
print(t9>=t10)

# immutable이지만
t11 =4.43,
t12 =3.97, 4.1, 3.27
print(t11 +t12) #임시로 출력하는 것
t11 = t11+t12 # t11+=t12 t11과 t12의 값을 더한 값을 t11에 새로운 값(주소)을 할당한 것.즉 t11이 할당 받은 id가 달라진다.
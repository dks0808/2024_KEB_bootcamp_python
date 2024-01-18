def squares(n):
    return n**2
even_numbers =[i for i in range(101) if i%2 ==0]
print(even_numbers)

print(tuple(map(squares, even_numbers))) #tuple을 왜 사용하지?
print(tuple(map(lambda x : x**2, even_numbers))) # map 첫 콤마에는 함수가 들어가는 자리 람다를 사용하면
# 람다는 익명의 함수이다.

z = lambda x : pow(x,2)
print(tuple(map(z, even_numbers)))
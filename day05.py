# '[Harry','Ron','Hermione']를 리스트 형태로 반환
def good(a):
     print(list(a))


name = 'Harry','Ron','Hermione'
z = 'Harry'
x = 'Ron'
c = 'Hermione'
q = z,x,c
good(name)
goodori(q)


# generator
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
ran = my_range(10)

for x in ran:
     if x%2==1:
          if x.count()==3:
               print(x)


# description






#in my brain
def get_odds(n):
     result = []
     for x in n :
          if x%2 ==1:
               result.append(x)
     print(result[2])


r = range(10)
get_odds(r)


hi

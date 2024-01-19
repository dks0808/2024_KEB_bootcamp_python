# '[Harry','Ron','Hermione']를 리스트 형태로 반환
def good(a)-> list:
    """
    chapter 9.1
    :param a: 
    :return: 
    """"
    harry_porter = input("enter the name").split() # 문자열을 split 해서 리스트로
    return harry_porter

    print(harry_porter)

# name = 'Harry','Ron','Hermione'
# z = 'Harry'
# x = 'Ron'
# c = 'Hermione'
# q = z,x,c
good()


# generator
# def my_range(first=0, last=100, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
# ran = my_range(100)
#
# for x in ran:
#      if x%2==1:
#           if x.count()==10:
#                print(x)
#
 #professer's code
def get_odds:
    for i in range(n,n+1,2):
        yield i

cnt = 0
odds =get_odds(9)
for odd in odds:
    cnt = cnt+1
    if cnt ==2:
        print(f'third number is {odd}')
        break
# description






#in my brain
# def get_odds(n):
#      result = []
#      for x in n :
#           if x%2 ==1:
#                result.append(x)
#      print(result[2])
#
#
# r = range(10)
# get_odds(r)


hi
#
@ deco

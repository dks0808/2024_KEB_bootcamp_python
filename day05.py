def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range(1,10)
print(ranger,type(ranger))
for x in ranger:
    print(x)

for reprint in ranger:
    print(reprint)

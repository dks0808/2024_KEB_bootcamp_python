# e2f = dick(dog='chien', cat='chat', walrus='morse')
# mans = dict(marx='russian', humist='bin', kant='g')
#
# # list(animal)
# print(e2f["walrus"])
# print(e2f.get('walrus'))
# print(list(e2f.keys()))
# e2f.update(mans)
# print(e2f)

# a = list(e2f.items())
#
# f2e = {a:b for b,a in e2f.items()}# comprehension
# print (f2e)
# print(f2e['chien'])
#
# #
# print(e2f.keys())
life = {'animals':{'cats':'Henri','octopi':'Grumpy','emus':'Lucy'},
 'plants':{'':''},
 'other':{'':''}}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])

squares = {i:i*i for i in range(10)}
print(squares)


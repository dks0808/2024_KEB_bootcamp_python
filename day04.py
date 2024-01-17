sugang = dict(python='kim', cpp='kang', db='kang')
# print(sugang)
# sugang['datastructure']= 'kim'
# print(sugang)
# sugang['datastructure']='park'
# print(sugang['db'])
# print(sugang.get('python'))
# print(sugang.get('opensource', 'not exist'))
for subject, professor in sugang.items():
    print(f"{subject}'s professor is {professor}")

for k in sugang.keys(): #keys를 안써줘도 키가자동으로나옴 키는 디폴트값임
    print(k)
for k in sugang:  # keys를 안써줘도 키가자동으로나옴 키는 디폴트값임
    print(k)
for v in sugang.values():
    print(v)

for v in sugang.items():# tuple 형태로 출력 packing
    print(v)
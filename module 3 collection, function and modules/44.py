
a = {'1':['a','b'], '2':['c','d']}

b = list(a.values())
for i in b[0]:
    for j in b[1]:
        print(i+j)

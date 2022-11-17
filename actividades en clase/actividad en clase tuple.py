import random
tam=round(random.randint(10,25))
tup=tuple(round(random.random()*100) for i in range(tam))
print(tup)
for i in tup:
    cont=0
    for j in range(1,i):
        if i%j==0:
            cont+=1
    if cont==1:
        print('primo',[i])
    else:
        print('no es primo',[i])
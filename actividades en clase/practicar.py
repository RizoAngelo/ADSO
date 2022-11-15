import random
s=0
vec=[]
for i in range(1,31):
    vec.append(round(random.randint(5,28)))
    s+=1
print(vec)
print(s)
for i in vec:
    print()

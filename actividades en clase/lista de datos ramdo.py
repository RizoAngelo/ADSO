import random
a=0
b=0
cont1=0
cont2=0
tam=int(input("digite numero "))
vec=[]
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
for i in range(len(vec)):
    if vec[i]%2==0:
        a+=1
        print(vec[i]," par",(a),"hay de par")
    else:
        b+=1
        print(vec[i]," impar",(b),"hay de impar")
        
        

        
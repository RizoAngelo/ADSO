num = int(input("Digite numero   "))
if num>0:
    print ("SUS DIVISORES SON: ")
    for i in range (1,num+1,1):
        if num%i==0:
            print (i)
elif num<0:
    print ("SUS DIVISORES SON: ")
    for i in range (-1,num-1,-1):
        if num%i==0:
            print (i)
else:
    print ("NINGÚN NÚMERO ES DIVISIBLE POR 0")
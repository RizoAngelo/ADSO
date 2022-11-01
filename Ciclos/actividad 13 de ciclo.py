A = int(input('digite los numeros: '))

c8 = A % 10
c7 = int((A % 100) / 10)
c6 = int((A % 1000) / 100)
c5 = int((A % 10000) / 1000)
c4 = int((A % 100000) / 10000)
c3 = int((A % 1000000) / 100000)
c2 = int((A % 10000000) / 1000000)
c1 = int((A - (A % 10000000)) / 10000000)

print(str(c8) +str(c7) +str(c6) +str(c5) +str(c4) +str(c3) +str(c2) +str(c1))
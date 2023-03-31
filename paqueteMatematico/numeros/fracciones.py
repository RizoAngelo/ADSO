def num_fraccion(numerador,denominador):
    frac=(str(numerador)+"/"+str(denominador))
    return frac

def suma_fraccion(n1,d1,n2,d2):
    r=0
    if d1==d2:
        r=str(n1+n2)+"/"+str(d2)
        return r
    else:
        r=str(n1*d2+n2*d1)+"/"+str(d2*d1)
        return r
def resta_fraccion(n1,d1,n2,d2):
    r=0
    if d1==d2:
        r=str(n1-n2)+"/"+str(d2)
        return r
    else:
        r=str(n1*d2-n2*d1)+"/"+str(d2*d1)
        return r
def multiplicacion_fraccion(n1,d1,n2,d2):
    r=str(n1*n2)+"/"+str(d2*d1)
    return r
def division_fraccion(n1,d1,n2,d2):
    r=str(n1*d2)+"/"+str(n2*d1)
    return r
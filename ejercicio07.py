def potencia(a,b):
    if b==1:
        return a
    else:
        if b % 2 == 0:
            z  = potencia(a, int(b/a))
            return z*z
        else:
            return a*potencia(a,b-1)
print(potencia(4,6))

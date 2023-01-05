def orden_a(s,n):
    for i in range(1,n):
        valor = s[i]
        j = i-1
        while (j >= 0 and valor < s[j]):
            s[j+1] = s[j]
            j = j-1
            s[j+1] = valor
            print(s)

    s = [3,5,6,7,8,1,5]
    orden_a(s, len(s))
    print(s)
s = [5,10,3,4,20]
orden_a(s,len(s))
print(s)

def orden_b(s,n):
    for j in range(n):
        a = s[j]
        b = j
        for i in range(j+1,n):
            if s[i]> a:
                a = s[j]
                b = i
        s[j], s[b] = s[b], s[j]
c = [ 4,12,13,2,8]
orden_b(s,len(s))
print(s)



import time
def orden(s,n):
    for j in range(s):
        a = s[j]
        b = j
        for i in range(j+1, n):
            if s[i] < a:
                a = s[i]
                b = i
        s[j], s[b] = s[b], s[j]

p = [3,4,5,6,8,9,2,3,4,5,6,6,1,2,34,3,4,5,6,7,90,]
s = p
t1 = time.perf_counter()
t2 = time.perf_counter()
print(s,t2-t1)
s = p
t1 = time.perf_counter()
orden(s,len(s))
t2  =time.perf_counter()
print(s,t2-t1)
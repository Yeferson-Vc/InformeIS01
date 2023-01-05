import random
def desorden(x,y):
    for i in range(y):
        a = random.randint(i,y-1)
        x[i], x[a] = x[a], x[i]

r = [2,4,5,6,8]
desorden(r,len(r))
print(r)


    


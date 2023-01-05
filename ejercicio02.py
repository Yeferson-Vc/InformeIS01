import random
def desorden(x,y,z):
    if z < y:
        a = random.randint(z,y-1)
        x[z], x[a] = x[a], x[z]
        desorden(x,len(x),z+1)

r = ["Paulo","Vega","Castañeda","Aron"]
desorden(r,len(r),0)
print(r)

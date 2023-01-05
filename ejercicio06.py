def robot(p):
    if p == 1 or p==2:
        return p
    return robot(p-1) + robot(p-2)
n = int(input("Cuantos metros caminara el robot: "))
for i in range(1,n+1):
    print(robot(i))
print(robot(17))

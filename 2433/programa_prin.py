a, b = map(int,input().split())
ultimo=0
for i in range(1, a+1):
    if(a % i == 0):
        for z in range(1, b+1):
            if(b % z == 0):
                if(z == i):
                    ultimo=z
print(ultimo)
    

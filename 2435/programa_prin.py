n = int(input())
primos=0
for i in range(1, n+1):
    co = 0
    for y in range(1,i+1):
        if(i % y == 0):
            co+=1
    if(co == 2):
        primos+=1
print(primos)


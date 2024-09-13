n = int(input())
a = 0
b = 1
con = 1
coni = 1
for i in range(1, n+1):
    if(i % 2 == 0):
        for y in range(1,con+1):
            print(b, end="")
        con+=1
        print(end=", ")
    else:
        for p in range(1, coni+1):
            print(a, end="")
        coni+=1
        print(end=", ")
n = int(input())
a = 0
b = 1
cero = 0
uno = 1
print(cero, end="")
for i in range(1, n+1):
    if(i % 2 == 0):
        for z in range(1, a+1):
            print(uno, end="")
        print(end=", ")
    else:
        for h in range(1, a+1):
            print(cero, end="")
        print(end=", ")
    c = a + b
    b = a
    a = c
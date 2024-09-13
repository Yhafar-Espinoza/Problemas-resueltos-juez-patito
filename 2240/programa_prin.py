n = int(input())
su = 0
a = 2
b = 1
for i in range(0, n):
    if (i % 2 == 0):
        su = su + a
        if(n == i+1):
            print(a, end=" = ")
        else:
            print(a,end=" - ")
        a = a + 2

    else:
        su = su - b
        if(n == i+1):
            print(b, end=" = ")
        else:
            print(b,end=" + ")
        b = b + 2
print(su)
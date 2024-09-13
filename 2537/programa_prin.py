n = int(input())
con=0
X = []
for y in range(n):
    X.append([0]*3)
for i in range(n):
    X[i]=list(map(int, input().split()[:3]))
for y in range(n):
    co = 0
    for i in range(3):
        if(X[y][i] == 1):
            co = co + 1
    if(co >= 2):
        con =con + 1
print(con)
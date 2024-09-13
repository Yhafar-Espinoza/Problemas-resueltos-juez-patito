a, b=map(int,input().split())
ma=max(a,b)
mi=min(a,b)
for i in range(ma,mi-1,-1):
    print(i)

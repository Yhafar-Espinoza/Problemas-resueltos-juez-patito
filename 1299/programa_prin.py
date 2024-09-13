for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    b=list(map(int,input().split()[:n]))
    su=0
    for p in range(len(a)):
        su=su+(a[p]*b[p])
    print(su)

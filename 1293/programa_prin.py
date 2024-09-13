for t in range(int(input())):
    b, c=map(int,input().split())
    lis=list(map(int,input().split()))
    su=0
    for i in range(b, c+1):
        su=su+lis[i]
    print(su)

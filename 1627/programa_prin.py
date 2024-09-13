for i in range(int(input())):
    a,b=map(int,input().split())
    ans=((a*(a+1))//2)*b
    print(ans)
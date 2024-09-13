n=1
while(n>=1):
    n=int(input())
    if(n!=0):
        lis=list(map(int,input().split()[:n]))
        print(sum(lis))

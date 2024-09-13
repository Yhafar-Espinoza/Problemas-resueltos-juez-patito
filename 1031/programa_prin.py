import statistics
while True:
     try:
        b=0
        n=int(input())
        lis=list(map(int,input().split()[:n]))
        s=len(lis)
        if(s%2==0):
            print("-1")
        else:
            a=statistics.median(lis)
            for i in range(len(lis)):
                if(lis[i]==a):
                    b=b+1
            if(b==1):
                print(a)
            else:
                print("-1")
     except EOFError:
          break



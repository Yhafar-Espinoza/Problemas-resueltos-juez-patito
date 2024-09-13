a, b, c=map(int,input().split())
c=c+1
if(c>59):
    c=0
    b=b+1
    if(b>59):
        b=0
        a=a+1
        if(a>23):
            a=0
            print("{:02d}:{:02d}:{:02d}".format(a, b, c))
        else:
            print("{:02d}:{:02d}:{:02d}".format(a, b, c))
    else:
        print("{:02d}:{:02d}:{:02d}".format(a, b, c))
else:   
    print("{:02d}:{:02d}:{:02d}".format(a, b, c))

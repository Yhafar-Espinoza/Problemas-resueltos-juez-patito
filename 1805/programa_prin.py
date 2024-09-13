for y in range(int(input())):
    a,b=map(float,input().split())
    if(b==1):
        su=a*0.12
        re=a-su
    elif(b==2):
        su=a*0.17
        re=a-su
    print("{:.2f}".format(re))

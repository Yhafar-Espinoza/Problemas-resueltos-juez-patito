for y in range(int(input())):
    n=input()
    m=len(n)
    m=m-1
    for i in range(len(n)):
        if(i==m):
            print(n[i],end="")
        else:
            print(n[i],end=",")
    print("")
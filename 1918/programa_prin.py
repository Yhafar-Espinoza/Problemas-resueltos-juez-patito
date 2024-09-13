for i in range(int(input())):
    n=input()
    a=len(n)
    a=a-1
    su=""
    for y in range(a,-1,-1):
        su=su+n[y]
    if(n==su):
        print(n)
    


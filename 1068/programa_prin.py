for o in range(int(input())):
    A=[]
    for i in range(int(input())):
        A.append(input())
    for p in range(len(A)):
        if(A[p]=="porque"):
            z=p
    print(z)
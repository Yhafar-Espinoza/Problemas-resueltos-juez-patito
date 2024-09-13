n=input()
lis=list(n)
su=""
a=0
for i in range(len(lis)):
    if(lis[i]=="u"):
        su=su+lis[i]
        if(a==7):
            a=0
    elif(a==7):
        su=su+lis[i]
        a=0
    a=a+1
print(su)
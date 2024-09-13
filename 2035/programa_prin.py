from collections import OrderedDict
lis=list(map(int,input().split()[:10]))
final= list(OrderedDict.fromkeys(lis))
print(len(final))
li=len(final)-1
for i in range(len(final)):
    if(li==i):
        print(final[i],end="")
    else:
        print(final[i],end=" ")
a,b=input().split()
la=list(a)
lb=list(b)
vp=[]
vi=[]
for i in range(len(la)):
    k=int(la[i])
    if(k%2==0):
        vp.append(la[i])
    else:
        vi.append(la[i])
for z in range(len(lb)):
    h=int(lb[z])
    if(h%2==0):
        vp.append(lb[z])
    else:
        vi.append(lb[z])
mip=int(min(vp))
maap=int(max(vp))
sup=""
for o in range(maap,mip-1,-1):
    for l in range(len(vp)):
        x=int(vp[l])
        if(o==x):
            sup=sup+vp[l]
mii=int(min(vi))
maai=int(max(vi))
sui=""
for o1 in range(maai,mii-1,-1):
    for l1 in range(len(vi)):
        x1=int(vi[l1])
        if(o1==x1):
            sui=sui+vi[l1]
print(sup,sui)
a,b,c,d,e,f=map(int,input().split())
coa=0;cob=0;coc=0;cod=0;coe=0;cof=0
if(a==0):
    coa=1
if(b==0):
    cob=1
if(c==0):
    coc=2
if(d==0):
    cod=2
if(e==0):
    coe=2
if(f==0):
    cof=8

if(a>1):
    while(a>1 and a!=0):
        a=a-1
        coa=coa-1
else:
    while(a<1 and a!=0):
        a=a+1
        coa=coa+1
if(b>1 and b!=0):
    while(b>1):
        b=b-1
        cob=cob-1
else:
    while(b<1 and b!=0):
        b=b+1
        cob=cob+1
if(c>2):
    while(c>2 and c!=0):
        c=c-1
        coc=coc-1
else:
    while(c<2 and c!=0):
        c=c+1
        coc=coc+1
if(d>2):
    while(d>2 and d!=0):
        d=d-1
        cod=cod-1
else:
    while(d<2 and d!=0):
        d=d+1
        cod=cod+1
if(e>2):
    while(e>2 and e!=0):
        e=e-1
        coe=coe-1
else:
    while(e<2 and e!=0):
        e=e+1
        coe=coe+1
if(f>8):
    while(f>8 and f!=0):
        f=f-1
        cof=cof-1
else:
    while(f<8 and f!=0):
        f=f+1
        cof=cof+1
print(coa,cob,coc,cod,coe,cof)
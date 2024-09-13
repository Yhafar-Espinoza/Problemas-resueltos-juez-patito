n=input()
s=list(n)
li=len(s)
li=li-1
su=""
for i in range(li,-1,-1):
    su=su+s[i]
print(su)
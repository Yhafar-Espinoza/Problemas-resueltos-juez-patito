n=input()
n=list(n)
for i in range(len(n)):
    s=i
if(s%2==0):
    s=s//2
    ep=n[s]
    print(ep)
else:
    print("*")

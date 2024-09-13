n=int(input())
lis=list(map(int,input().split()[:n]))
li=len(lis)
li=li-1
A=[]
for i in range(li,-1,-1):
	A.append(lis[i])
if (lis==A):
	print('SI')
else:
	print('NO')

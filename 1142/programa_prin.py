A,B,N=map(int,input().split())
for i in range(N-2):
    c=B*B + A
    A=B
    B=c
print(c)

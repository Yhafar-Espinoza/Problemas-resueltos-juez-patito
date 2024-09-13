n, cambio=map(int,input().split())
copia=n
A=[]
cambio=cambio-1
while(n>0):
    if(n==1):
        A.append(1)
    else:
        mo=n%2
        A.append(mo)
    n=n//2
z=len(A)
z=z-1
re=""
B=[]
for i in range(z,-1,-1):
    B.append(A[i])
for y in range(len(B)):
    if(y==cambio):
        if(B[y]==1):
            B[y]=0
        else:
            B[y]=1
for y1 in range(len(B)):
    x=str(B[y1])
    re=re+x
print(re)      
numero_binario = re
numero_decimal = 0 
for posicion, digito_string in enumerate(numero_binario[::-1]):
	numero_decimal += int(digito_string) * 2 ** posicion
print(numero_decimal)





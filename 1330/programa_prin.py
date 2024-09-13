n = input().split()
rotaciones = int(n[1])
frase = n[0]
p = (frase[:-1])                
u = frase[-1]                  
nuevo = frase                   
for i in range(rotaciones):
    nuevo = u + p               
    u = nuevo[-1]             
    p = nuevo[:-1]              
print(nuevo)
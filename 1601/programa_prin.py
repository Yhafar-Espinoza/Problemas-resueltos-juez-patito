casos = int(input())
for i in range(casos):
    x =input()                 
    if x == x[::-1]:            
        print('SI')
    else:
        print('NO')

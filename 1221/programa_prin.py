a, b ,c = map(int,input().split())
ma=max(a,b,c)
mi=min(a,b,c)
me=(a+b+c)-(ma+mi)
print(mi,me,ma)
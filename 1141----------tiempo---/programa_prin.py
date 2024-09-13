while True:
	try:
		n, ro=map(int,input().split())
		A=[]
		while(n>0):
			if(n==1):
				A.append(1)
			else:
				mo=n%2
				A.append(mo)
			n=n//2
		z=len(A)
		me=8-z
		si=""
		z=z-1
		for i in range(z,-1,-1):
			x=str(A[i])
			si=si+x
		ceros=""
		for y in range(1,me+1):
			ceros=ceros+"0"
		nuevo=ceros+si
		nuevo=list(nuevo)
		x3=len(nuevo)
		x3=x3-1
		for i1 in range(1,ro+1):
			aux=nuevo[0]
			for i3 in range(len(nuevo)-1):
				nuevo[i3]=nuevo[i3+1]
			nuevo[x3]=aux
		final=""
		for i4 in range(len(nuevo)):
			final=final+nuevo[i4]
		numero_binario = final
		numero_decimal = 0 
		for posicion, digito_string in enumerate(numero_binario[::-1]):
			numero_decimal += int(digito_string) * 2 ** posicion
		print(numero_decimal)
	except EOFError:
		break

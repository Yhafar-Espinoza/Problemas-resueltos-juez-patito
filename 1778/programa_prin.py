dic={"a":"@","b":"8","c":"(","d":"|)","e":"3","f":"#","g":"6","h":"[-]","i":"|","j":"_|","k":"|<","l":"1","m":"[]\/[]","n":"[]\[]","o":"0","p":"|D","q":"(,)","r":"|z","s":"$","t":"']['","u":"|_|","v":"\/","w":"\/\/","x":"}{","y":"`/","z":"2"}
z=input()
for i in range(len(z)):
    x=z[i]
    if(x=="a" or x=="b" or x=="c" or x=="d" or x=="e" or x=="f" or x=="g" or x=="h" or x=="i" or x=="j" or x=="k" or x=="l" or x=="m" or x=="n" or x=="o" or x=="p" or x=="q" or x=="r" or x=="s" or x=="t" or x=="u" or x=="v" or x=="w" or x=="x" or x=="y" or x=="z"):
        print(dic[z[i]],end="")
    else:
        print(z[i],end="")
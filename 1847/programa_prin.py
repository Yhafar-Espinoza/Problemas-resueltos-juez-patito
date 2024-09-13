for y in range(int(input())):
    n=input()
    su=""
    for i in range(len(n)):
        if(n[i]=="M"):
            su=su+"0"
        elif(n[i]=="U"):
            su=su+"1"
        elif(n[i]=="R"):
            su=su+"2"
        elif(n[i]=="C"):
            su=su+"3"
        elif(n[i]=="I"):
            su=su+"4"
        elif(n[i]=="E"):
            su=su+"5"
        elif(n[i]=="L"):
            su=su+"6"
        elif(n[i]=="A"):
            su=su+"7"
        elif(n[i]=="G"):
            su=su+"8"
        elif(n[i]=="O"):
            su=su+"9"
        else:
            su=su+n[i]
    print(su)
    
        
                
                
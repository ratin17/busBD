
url="stopsData.txt"
iStop=input("Enter Destination :")

def findStops(stop):
    file=open(url,"r")
    rawStops=file.read()

    stops=rawStops.split("> <")
    n=len(stops)
    v=5

    match=dict()

    c=[]
    for z in range(26):
        c.append(0)
    
    for s in stop:
        p=ord(s)
        if (p>=97 and p<=122):
            c[p-97]+=1
        elif (p>=65 and p<=90):
            c[p-65]+=1
    
    for j in range(n):
        temp=stops[j]

        d=[]
        for z in range(26):
            d.append(0)
    
        for t in temp:
            q=ord(t)
            if (q>=97 and q<=122):
                d[q-97]+=1
            elif (q>=65 and q<=90):
                d[q-65]+=1
    
        
        dif=0
        for k in range(26):
            dif+=abs(c[k]-d[k])
        
        if dif<v:
            match[str(temp)]=dif


    if len(match)>0:
        print(f'\n{len(match)} match found\n')
        
        # SMatch=sorted(match)
        SMatch = sorted(match.items(), key=lambda x:x[1])
        fMatch=dict(SMatch)

        for key,val in fMatch.items():
            print(key,val)
    
    else:
        print("No Match Found !")


findStops(iStop)


su="BusBD\stopsData.txt"

sf=open(su,"r")
stops=sf.read().split("> <")
sf.close()

v=4

n=len(stops)

for i in range(n):
    stop=stops[i]
    match=[]
    match.append(stop)

    c=[]
    for z in range(26):
        c.append(0)
    
    for s in stop:
        p=ord(s)
        if (p>=97 and p<=122):
            c[p-97]+=1
        elif (p>=65 and p<=90):
            c[p-65]+=1
    
    for j in range(i+1,n):
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
            match.append(temp)
    if len(match)>1:
        print(match)

blackSheep=['CMirpur 14','Sony Cenema Hall','Sony CInema Hall','Natun Bazar','Dia Bari','Karwan Bazar','kakali','Asad gate','Malibagg Mor','Kalabagan','Malibagh Rail Gate','Shanir Akhra','Sat rasta','AKeraniganj','Ring Road','ashantek','Aminbazar']
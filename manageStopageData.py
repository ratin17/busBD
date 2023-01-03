
def mergeStopages(Istops):

    url="G:\Projects\BusBD\stopagesData.txt"

    f = open(url, "r")
    Ilines=f.read()
    f.close()
    
    if len(Ilines)>0:
        lines=Ilines.split("> <")
    else: lines=[]
    
    prev=len(lines)
    print(f'\nPrev: {prev}, Try: ',end="")

    stops=Istops.split("⇄")

    print(f'{len(stops)}, Tot: ',end="")

    for stop in stops:
        pStop=stop.strip()
        if pStop not in lines:
            lines.append(pStop)
    
    print(f'{len(lines)}, Eli: {prev+len(stops)-len(lines)}\n')
    
    #print(lines)


    f = open(url, "w")
    for i in range(len(lines)):
        f.write(lines[i])
        if i<(len(lines)-1):
            f.write("> <")
    
    f.close()
    



raw="College Gate ⇄ Shishu Mela ⇄ Shyamoli ⇄ Kallyanpur ⇄ Darussalam ⇄ Technical ⇄ Bangla College ⇄ Tolarbag ⇄ Ansar Camp ⇄ Mirpur 1 ⇄ Sony Cinema Hall ⇄ Mirpur 2 ⇄ Proshika Moor ⇄ Pallabi ⇄ Mirpur 12"


mergeStopages(raw)

su="G:\Projects\BusBD\pData1.txt"

blackSheep=['CMirpur 14','Sony Cenema Hall','Sony CInema Hall','Natun Bazar','Dia Bari','Karwan Bazar','kakali','Asad gate','Malibagg Mor','Kalabagan','Malibagh Rail Gate','Shanir Akhra','Sat rasta','AKeraniganj','Ring Road','ashantek','Aminbazar']

sf=open(su,"r")
stops=sf.read().split("> <")
sf.close()

l1=len(stops)

new=[]

for stop in stops:
    if stop not in new:
        if stop not in blackSheep:
            new.append(stop)

l2=len(new)

f = open(su, "w")
for i in range(l2):
    f.write(new[i])
    if i<(l2-1):
        f.write("> <")
    
f.close()

print(f'Reduced : {l1-l2} , New: {l2}')

from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_20290_B.txt')

data=[]
for line in f:
    x,y=[float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))

clusters=[]
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi=[p1 for p1 in data if dist(p,p1)<=0.5]
        clusters[-1]+=sosedi
        for p1 in sosedi: data.remove(p1)
    print(len(clusters[-1]))

clusters=[cl for cl in clusters if len(cl)>1896]
print([len(cl) for cl in clusters])

def krai(cl):
    m=[]
    for p in cl:
        sm=sum([dist(p,p1) for p1 in cl])
        m.append([sm,p])
    return max(m)[1]

krais=[krai(cl) for cl in clusters]
Tx=int(abs((sum([x for x,y in krais])/len(krais))*10000))
Ty=int(abs((sum([y for x,y in krais])/len(krais))*10000))
print(Tx,Ty)

# 11575 4282
# 4228 16951
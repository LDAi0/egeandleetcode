#0,4 0,1
from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_19647_B.txt')

data=[]
for line in f:
    x,y=[float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))

clusters=[]
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi=[p1 for p1 in data if dist(p,p1)<0.1]
        clusters[-1]+=sosedi
        for p1 in sosedi: data.remove(p1)
    print(len(clusters[-1]))
def down_centr(cl):
    m=[]
    for p in cl:
        sm=sum([dist(p,p1) for p1 in cl])
        m.append([sm,p])
    return min(m)[1]
data=clusters[0]+clusters[1]+clusters[2]
print(len(data))
down_centrs=[down_centr(cl) for cl in clusters]
print(down_centrs)
def trans_f(d):
    m=[]
    for p in d:
        m.append([dist(p,down_centrs[0])+dist(p,down_centrs[1])+dist(p,down_centrs[2]),p])
    return min(m)[1]
trans=trans_f(data)
print(trans)
Px=round(trans[0]*10000)
Py=round(trans[1]*10000)
print(Px,Py)
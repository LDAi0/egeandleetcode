from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_20130_B.txt')

data=[]
for line in f:
    x,y=[float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))

clusters=[]
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi=[p1 for p1 in data if dist(p,p1)<=0.7]
        clusters[-1]+=sosedi
        for p1 in sosedi: data.remove(p1)
    print(len(clusters[-1]))

def find_d(cl):
    m=[]
    for p in cl:
        for p1 in cl:
            m.append([dist(p,p1),p,p1])
    return max(m)[1:]
t=[find_d(cl) for cl in clusters]
print(t)
ds=[]
for p in t:
    for p1 in p:
        ds.append(p1)
print(ds)
Px=int(  (sum([x for x,y in ds])/len(ds))*10000  )
Py=int(  (sum([y for x,y in ds])/len(ds))*10000  )
print(Px,Py)
# 16730 48696
# 23982 47539
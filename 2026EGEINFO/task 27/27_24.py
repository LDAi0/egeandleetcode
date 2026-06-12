from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_20295_B.txt')

data=[]
for line in f:
    x,y=[float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))

clusters=[]
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi=[p1 for p1 in data if dist(p,p1)<=0.4]
        clusters[-1]+=sosedi
        for p1 in sosedi: data.remove(p1)
    print(len(clusters[-1]))

def find_V(cl): 
    m=[]
    for p in cl:
        m.append(len([p1 for p1 in cl if dist(p,p1)<=1]))
    return sum(m)/len(m)
Vs=[find_V(cl) for cl in clusters]
print(Vs)
Pmin=int(min(Vs)*100_000)
Pavg=int(  (sum(Vs)/len(Vs))*100_000  )
print(Pmin,Pavg)
# 5158000 9476083
# 7604400 18899514
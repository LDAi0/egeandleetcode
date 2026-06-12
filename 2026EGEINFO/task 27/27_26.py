from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_20294_B.txt')

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

def find_isolated(cl):
    m=[]
    for p in cl:
        kolvo=len([p1 for p1 in cl if dist(p,p1)<=1])
        m.append([kolvo,p[1],p])
    return min(m)[2]
isolateds=[find_isolated(cl) for cl in clusters]
Px=int(abs(  (sum([x for x,y in isolateds])/len(isolateds))*100_000  ))
Py=int(abs(  (sum([y for x,y in isolateds])/len(isolateds))*100_000  ))
print(Px,Py)
# 135491 131265
# 232818 15126

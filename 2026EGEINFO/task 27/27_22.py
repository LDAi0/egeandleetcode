from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_20293_B.txt')

data=[]
for line in f:
    x,y=[float(k) for k in line.split()]
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

def find_nav(cl):
    m=[]
    for p in cl:
        kolvo=len([p1 for p1 in cl if dist(p,p1)<=1])
        m.append([kolvo,p])
    return max(m)[1]
navs=[find_nav(cl) for cl in clusters]
print(navs)
Px=int(abs(  (sum([x for x,y in navs])/len(navs))*100_000  ))
Py=int(abs(  (sum([y for x,y in navs])/len(navs))*100_000  ))
print(Px,Py)
# 171553 32527
# 157853 13516



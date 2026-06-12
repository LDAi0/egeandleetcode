from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_20292_A.txt')

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

def sr(cl):
    m=[]
    for l in range(0,len(cl)-1):
        for r in range(l+1,len(cl)):
            m.append(dist(cl[l],cl[r]))
    return sum(m)/len(m)
srs=[sr(cl) for cl in clusters]
Smin=int(min(srs)*100_000)
Smax=int(max(srs)*100_000)
print(Smin,Smax)

# 79724 158994
# 205908 237869
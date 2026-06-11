from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_20291_B.txt')

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

def diametr(cl):
    return max([dist(p,p1) for p in cl for p1 in cl])

diametrs=[diametr(cl) for cl in clusters]
print(diametrs)
Dmin=int(min(diametrs)*100_000)
Davg=int((sum(diametrs)/len(diametrs))*100_000)
print(Dmin,Davg)
# 208364 305606
# 544492 600793
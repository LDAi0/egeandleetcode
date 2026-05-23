from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_18627_B.txt')
print('temp')
data=[]
for line in f:
    x,y=[float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))

clusters=[]
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi=[p1 for p1 in data if dist(p,p1)<=1]
        clusters[-1]+=sosedi
        for p1 in sosedi: data.remove(p1)
    print(len(clusters[-1]))

def centroid(cl):
    m=[]
    for p in cl:
        sm=sum(dist(p,p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]
centroids=[centroid(cl) for cl in clusters]
print(centroids)
Px=int(sum(x for x,y in centroids)/len(centroids)*100000)
Py=int(sum(y for x,y in centroids)/len(centroids)*100000)
print(Px,Py)
# 752263 548854
# 767186 281688
from math import dist
f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 14/task_25444_B.txt')

data=[]
for line in f:
    x,y=[float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))

clusters=[]
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi=[p1 for p1 in data if dist(p,p1)<=0.2]
        clusters[-1]+=sosedi
        for p1 in sosedi: data.remove(p1)
    print(len(clusters[-1]))

clusters=[cl for cl in clusters if len(cl)>=10]

def centroid(cl):
    m=[]
    for p in cl:
        sm=sum([dist(p,p1) for p1 in cl])
        m.append([sm,p])
    return min(m)[1]

centroids=[centroid(cl) for cl in clusters]

Q1=min(dist(centroids[0],centroids[1]),dist(centroids[0],centroids[2]),dist(centroids[1],centroids[2]))
Q2=max(dist(centroids[0],centroids[1]),dist(centroids[0],centroids[2]),dist(centroids[1],centroids[2]))
print(abs(int(Q1*10000)),abs(int(Q2*10000)))
# d1=max(dist(centroids[0],p) for p in clusters[1])
# d2=max(dist(centroids[1],p) for p in clusters[0])
# P1=abs(int(max(d1,d2)*10000))
# print(P1)

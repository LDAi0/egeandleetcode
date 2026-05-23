from math import dist
f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 13/task_23384_B.txt')

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
clusters=[cl for cl in clusters if len(cl)>10]
print([len(cl) for cl in clusters])
def centroid(cl):
    m=[]
    for p in cl:
        sm=sum(dist(p,p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]
centroids=[centroid(cl) for cl in clusters]

m=[]
for cd in centroids:
    m.append(dist(cd,[0,0]))
Q1=abs(int(min(m)*10000))
Q2=abs(int(max(m)*10000))
print(Q1,Q2)




# Px=abs(int((centroids[0][0]+centroids[1][0])*10000))
# Py=abs(int((centroids[0][1]+centroids[1][1])*10000))
# print(Px,Py)
# 110156 196632
# 224871 273226
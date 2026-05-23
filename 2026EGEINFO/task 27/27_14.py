from math import dist 
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_25447_B.txt')
print('trmepo')

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
for cl in clusters:
    print(len(cl))
def centroid(cl):
    m=[]
    for p in cl:
        sm=sum(dist(p,p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]
centroids=[centroid(cl) for cl in clusters]

sr_min=[]
for p in clusters[2]:
    if centroids[2]!=p:
        sr_min.append(dist(centroids[2],p))
Q1=abs(int(sum(sr_min)/len(sr_min)*10000))
sr_max=[]
for p in clusters[0]:
    if centroids[0]!=p:
        sr_max.append(dist(centroids[0],p))
Q2=abs(int(sum(sr_max)/len(sr_max)*10000))
print(Q1,Q2)

# Px=abs(int(min(centroids[i][0] for i in range(0,len(centroids)))*10000))
# Py=abs(int(min(centroids[i][1] for i in range(0,len(centroids)))*10000))
# print(Px,Py)
# 115252 58612
# 9202 8993
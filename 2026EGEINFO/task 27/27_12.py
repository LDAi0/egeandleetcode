from math import dist 
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_25445_B.txt')
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
    print(len(clusters[-1]))
clusters=[cl for cl in clusters if len(cl)>10]
def centroid(cl):
    m=[]
    for p in cl:
        sm=sum(dist(p,p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]
centroids=[centroid(cl) for cl in clusters]

Qx=abs(int(sum(x for x,y in centroids)/len(centroids)*10000))
Qy=abs(int(sum(y for x,y in centroids)/len(centroids)*10000))
print(Qx,Qy)

# Px=abs(int((centroids[0][0]-centroids[1][0])*10000))
# Py=abs(int((centroids[0][1]-centroids[1][1])*10000))
# print(Px,Py)
# 27784 104799
# 210416 136231

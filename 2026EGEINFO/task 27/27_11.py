from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_25441_B.txt')
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
        sosedi=[p1 for p1 in data if dist(p,p1)<=0.2]
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
print(centroids)

m=[]
for i in range(0,len(clusters)):
    m.append(max(dist(centroids[i],p) for p in clusters[i]))
Q2=abs(int(max(m)*10000))
Q1=abs(int(dist(centroids[0],centroids[1])*10000))
print(Q1,Q2)

# Px=abs(int(abs(centroids[0][0]-centroids[1][0])*10000))
# Py=abs(int(abs(centroids[0][1]-centroids[1][1])*10000))
# print(Px,Py)
# 18236 93042
# 9163 1646

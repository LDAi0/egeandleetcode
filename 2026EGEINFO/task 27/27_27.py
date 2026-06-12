from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_20205_B.txt')
data=[]
print('temp')
for line in f:
    x,y=[float(p) for p in line.split()]
    data.append([x,y])
print(len(data))
# sr1=int((sum([dist(centr1bh,p)-3 for p in bh1])/len(bh1))*1000)
# sr2=int((sum([dist(centr2bh,p)-4 for p in bh2])/len(bh2))*1000)
# sr3=int((sum([dist(centr3bh,p)-5 for p in bh3])/len(bh3))*1000)
clusters=[]
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p0 for p0 in data if dist(p,p0)<=0.5]
        clusters[-1]+=sosedi
        for p2 in sosedi: data.remove(p2)
    print(len(clusters[-1]))

def centroid(cl):
    m=[]
    for p in cl:
        sm=sum(dist(p,f) for f in cl)
        m.append([sm,p])
    return max(m)[1]

centroids=[centroid(cl) for cl in clusters]
print(centroids)
Px= int(sum(x for x,y in centroids)/len(centroids)*10000)
Py= int(sum(y for x,y in centroids)/len(centroids)*10000)
print(Px,Py)
# 12777 1129
# 8059 21704
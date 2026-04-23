from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\27880.txt')

print('temp')
data=[]
for line in f:
    line=line.replace(',','.')
    x,y=[float(k) for k in line.split()]
    data.append([x,y])
print(len(data))

clusters=[]
while len(data)!=0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi=[p1 for p1 in data if dist(p,p1)<0.1]
        clusters[-1].extend(sosedi)
        for x in sosedi: data.remove(x)
for cl in clusters:
    if len(cl)<10: clusters.remove(cl)
for cl in clusters:
    if len(cl)<10: clusters.remove(cl)
print([len(cl) for cl in clusters])      

def centroid(cl):
    m=[]
    for p in cl:
        sm=sum(dist(p,p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]
centroids=[centroid(cl) for cl in clusters]
#print(abs((min([dist(centroids[0],p) for p in clusters[1]])*10000)//1))
#print(abs((min([dist(centroids[1],p) for p in clusters[0]])*10000)//1))
#print(abs((max([dist(centroids[0],p) for p in clusters[1]])*10000)//1))
#print(abs((max([dist(centroids[1],p) for p in clusters[0]])*10000)//1))

print(abs(((min(dist(centroids[0],centroids[1]),dist(centroids[1],centroids[2]),dist(centroids[0],centroids[2])))*10000)//1))
print(abs(((max(dist(centroids[0],centroids[1]),dist(centroids[1],centroids[2]),dist(centroids[0],centroids[2])))*10000)//1))



f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_18314_B.txt')
def d(a,b):
    return abs(b[0]-a[0])+abs(b[1]-a[1])

data=[]
for line in f:
    x,y=[float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))

clusters=[]
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi=[p1 for p1 in data if d(p,p1)<=2]
        clusters[-1]+=sosedi
        for p1 in sosedi: data.remove(p1)
    print(len(clusters[-1]))

def centroid(cl):
    m=[]
    for p in cl:
        sm=sum([d(p,p1) for p1 in cl])
        m.append([sm,p])
    return min(m)[1]

centroids=[centroid(cl) for cl in clusters]
print(centroids)
Px=int(abs( (sum([x for x,y in centroids])/len(centroids))*1000  ))
Py=int(abs( (sum([y for x,y in centroids])/len(centroids))*1000  ))
print(Px,Py)

# 23509 554
# 3078 4758
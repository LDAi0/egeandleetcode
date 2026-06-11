from math import dist
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_20207_B.txt')

data=[]
for line in f:
    x,y=[float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))

clusters=[]
while data:
    clusters.append([data.pop(0)])
    for p1 in clusters[-1]:
        sosedi=[p for p in data if dist(p,p1)<=1]
        clusters[-1]+=sosedi
        for p in sosedi: data.remove(p)
    print(len(clusters[-1]))

def mediana_x(cl):
    for p in cl:
        mr=[p1 for p1 in cl if p!=p1 and p1[0]>p[0]]
        ls=[p1 for p1 in cl if p!=p1 and p1[0]<p[0]]
        if len(mr)==len(ls):
            return p
def mediana_y(cl):
    for p in cl:
        mr=[p1 for p1 in cl if p!=p1 and p1[1]>p[1]]
        ls=[p1 for p1 in cl if p!=p1 and p1[1]<p[1]]
        if len(mr)==len(ls):
            return p
medians_x=[mediana_x(cl) for cl in clusters]
medians_y=[mediana_y(cl) for cl in clusters]
Px=int((sum([x for x,y in medians_x])/len(medians_x))*10000 )
Py=int((sum([y for x,y in medians_y])/len(medians_y))*10000 )
print(Px,Py)
# 40893 9686
# 30438 41916
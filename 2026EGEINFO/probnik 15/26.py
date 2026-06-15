f=open(r'C:\Users\abso\Documents\Visual Studio\GoLeetcode\2026EGEINFO\probnik 15\task_19256_A.txt')
kolvo=int(f.readline())
data=[]
print('temmp')
for line in f:
    x,y=[int(k) for k in line.split()]
    data.append([x,y])
data=sorted(data)
print(len(data),kolvo, data)
res=[[0,[0],[0]]]
temp=-1
for p in data:
    if p[0]!=res[-1][0]:
        res.append([p[0],[p[1]],[1]])
    else:
        if p[1]-res[-1][1][-1]==1:
            res[-1][1].append(p[1])
            res[-1][2][-1]+=1
        else:
            res[-1][2].append(1)
print(res)
mx=[]
for p in res:
    mx.append([max(p[2]),p[0]])
print(sorted(mx))

f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 12/task_7089_A.txt')
a=[int(x) for x in f]
mn=min(a)
res=[]
for i in range(0,len(a)-1):
    if (a[i]%111==mn)or(a[i+1]%111==mn):
        res.append(a[i]+a[i+1])
print(len(res),min(res))
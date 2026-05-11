f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\probnik 10\\task_7267_A.txt')
a=[int(x) for x in f]
mn=min(a)
res=[]
for i in range(0,len(a)-1):
    if (a[i]%117==mn) or (a[i+1]%117==mn):
        res.append(a[i]+a[i+1])
print('temp', len(res), max(res))

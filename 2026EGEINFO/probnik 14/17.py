f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 14/task_9070_A.txt')
a=[int(line) for line in f]
temp=[0]
a=temp+a
res=[]
mn=min([x for x in a if 100<=x<=999 and len(set(str(x)))==len(str(x))])
for i in range(1,len(a)//2+1):
    if (a[i]*a[-i])%mn==0:
        res.append(a[i]+a[-i])
print(len(res),min(res))

f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 9/task_11481_A.txt')
a=[int(x) for x in f]
mx=max([x for x in a if str(abs(x))[0]=='8' ])
res=[]
for i in range(0,len(a)-2):
    if (str(abs(a[i]))[0]=='6')+(str(abs(a[i+1]))[0]=='6' )+(str(abs(a[i+2]))[0]=='6')<=1:
        if (a[i]+a[i+1]+a[i+2])>=mx:
            res.append(a[i]+a[i+1]+a[i+2])
print(len(res),max(res))
f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 14/task_13715_A.txt').readline()
m=0
for l in range(0,len(f)):
    for r in range(l+m,len(f)):
        c=f[l+1:r]
        if c.count('AB')>50: break
        if c.count('AB')==50: m=len(c)
print(m)
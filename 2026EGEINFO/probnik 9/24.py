f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 9/task_23281_A.txt').readline()
m=0
for l in range(0,len(f)):
    for r in range(l+m,len(f)):
        c=f[l:r+1]
        cnt=c.count('Y')
        if cnt>80: break
        if c.count('2025')>=90 and cnt==80:
            m=len(c)
print(m)

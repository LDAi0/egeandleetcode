s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_14643_A.txt').readline()

m=0
for l in range(0,len(s)):
    for r in range(l+m,len(s)):
        c=s[l:r+1]
        if 'AXMM' in c: break
        m=max(len(c),m)
print(m)
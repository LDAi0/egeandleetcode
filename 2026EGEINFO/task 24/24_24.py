s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_9075_A.txt').readline()
m=0
for i in '02468': s=s.replace(i,'2')
for i in '13579': s=s.replace(i,'1')
for l in range(0,len(s)):
    for r in range(l+m,len(s)):
        c=s[l:r+1]
        if '21' in c or '12' in c: break
        m=max(len(c),m)
print(m)

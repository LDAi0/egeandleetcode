s=open(r'C:\Users\abso\Documents\Visual Studio\GoLeetcode\2026EGEINFO\probnik 15\task_9845_A.txt').readline()
for c in 'AB': s=s.replace(c,'C')
s=s.replace('8','9')
m=0
for l in range(0,len(s)):
    for r in range(l+m,len(s)):
        c=s[l:r+1]
        if 'CC' in c or '99' in c: break
        m=max(len(c),m)
print('temp',m)
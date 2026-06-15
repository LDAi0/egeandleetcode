s=open(r'C:\Users\abso\Documents\Visual Studio\GoLeetcode\2026EGEINFO\task 24\task_12476_A.txt').readline()
m=0
for l in range(0,len(s)):
    for r in range(l+m,len(s)):
        c=s[l:r+1]
        if c.count('RO')>21: break
        if c.count('ORO')>=1 or c.count('ROR')>=1: break
        m=max(len(c),m)
print(m)
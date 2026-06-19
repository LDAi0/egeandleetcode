s=open(r'C:\Users\abso\Documents\Visual Studio\GoLeetcode\2026EGEINFO\probnik last\task_20909_A.txt').readline()
m=0
for l in range(0,len(s)):
    for r in range(l+m,len(s)):
        c=s[l:r+1]
        if c.count('AB')>100: break
        if c.count('AB')==100: m=max(len(c),m)
print(m)
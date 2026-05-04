f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 7\\1.txt').readline()

m=0
for l in range(0,len(f)):
    for r in range(l+m,len(f)):
        c=f[l:r+1]
        if c.count('AB')>50: break
        if c.count('AB')==50:
            m=len(c)
print('',m)
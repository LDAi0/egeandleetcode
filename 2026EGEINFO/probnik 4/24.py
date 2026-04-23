f=open("C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 4\\1.txt").readline()
f=f.replace('P','1')
f=f.replace('R','2')

m=0
for l in range(len(f)):
    for r in range(l+m,len(f)):
        c=f[l:r+1]
        if '12' in c or '21' in c: break
        m=len(c)
print('temp',m)
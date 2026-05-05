f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 8\\1.txt').readline()
f=f.replace('*','+')
m=0
for l in range(0,len(f)):
    for r in range(l+m,len(f)):
        c=f[l:r+1]
        if '++' in c:
            break
        m=len(c)
print('temp',m)
        
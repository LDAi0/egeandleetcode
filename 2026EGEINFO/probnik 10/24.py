f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 10\\task_4602_A.txt').readline()
m=0
for c in 'AO': f=f.replace(c,'a')
for c in 'BCD': f=f.replace(c,'b')

for l in range(0,len(f)):
    for r in range(l+m,len(f)):
        c=f[l:r+1]
        if 'bb' in c or 'aa' in c or c[0]=='a': break
        m=len(c)
print('tmep', m)
res=[]
for i in range(0,len(f)-1):
    if f[i]=='b' and f[i+1]=='a': m+=2
    else:
        res.append(m)
        m=0
print(max(res))
file=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 2\\24.txt').readline()
res=[]
m=0
for i in range(0,len(file)):
    for l in range(i+m,len(file)):
        c=file[i:l+1]
        if c.count('T')>100: break
        m=len(c)
print('temp', m)
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 6\\1.txt').readline()
print('temp')
for x in 'CDF': f=f.replace(x,'C')
for x in 'AO': f=f.replace(x,'A')
cnt_max=0
cnt_temp=0
for i in range(0,len(f)-1):


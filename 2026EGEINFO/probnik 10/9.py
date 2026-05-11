f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 10\\1.txt')
cnt=0
for line in f:
    a=[int(x) for x in line.split()]
    if max(a)+min(a)<(sum(a)-(max(a)+min(a))):
        cnt+=1
print('temp',cnt)
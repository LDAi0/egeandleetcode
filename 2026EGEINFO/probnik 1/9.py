cnt=0
for line in open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 1\\9.txt'):
    a=[int(x) for x in line.split()]
    if (max(a)+min(a))*2<=sum(a):
        cnt+=1
print('temp', cnt)
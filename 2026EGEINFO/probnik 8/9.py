
cnt=0
for line in open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 8\\1.txt'):
    a=[int(x) for x in line.split()]
    nepov=[x for x in a if a.count(x)==1]
    if ((len(nepov)==5)+( ( ( max(a) + min(a) ) *2 ) < ( sum(a) - (max(a)+min(a)) ) ))==1:
        cnt+=1
print('temp',cnt)
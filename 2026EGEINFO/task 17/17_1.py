s=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 17\\1.txt')
a=[int(x) for x in s]
mn=min(a)
cnt=0
mnsum=1000000000
for i in range(0,len(a)-1):
    if a[i]%111==mn or a[i+1]%111==mn:
        cnt+=1
        mnsum=min(mnsum,a[i]+a[i+1])
print('temp', cnt,mnsum)


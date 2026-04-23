s=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 17\\1.txt')
a=[int(x) for x in s]
print('temp')
res=[]
for i in range(0,len(a)-3):
    if ((abs(a[i])%100==13) + (abs(a[i+3])%100==13))==1:
        res.append(a[i]+a[i+3])
print(len(res),max(res))
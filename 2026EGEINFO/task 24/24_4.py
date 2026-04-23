s=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 24\\24_123123.txt').readline()
print('temp')
res=[]
m=0
for l in range(0,len(s)-3):
    for n in range(l+m,len(s)-3):
        c=s[l:n+1]
        if c[n]
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 11\\1.txt').readline()
f=f+'0'
mx=0
tp=0
for i in range(0,len(f)):
    if f[i]=='K' and f[i+1]=='L':
        tp+=1
        mx=max(mx,tp+1)
        continue
    if f[i]=='L' and f[i+1]=='M':
        tp+=1
        mx=max(mx,tp+1)
        continue
    if f[i]=='M' and f[i+1]=='N':
        tp+=1
        mx=max(mx,tp+1)
        continue
    if f[i]=='N' and f[i+1]=='K':
        tp+=1
        mx=max(mx,tp+1)
        continue
    mx=max(mx,tp+1)
    tp=0
print('temp',mx)
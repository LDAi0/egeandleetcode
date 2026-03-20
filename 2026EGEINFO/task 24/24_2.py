s=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 24\\24_123123.txt').readline()

ans=0
t=0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        t+=1
    else:
        ans=max(ans,t)
        t=0
print('temp',ans)
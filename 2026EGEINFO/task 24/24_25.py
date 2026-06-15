s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/24.txt').readline()

cnt=0
l=0
for r in range(4,len(s)):
    if s[r-4]==s[r-2]==s[r] and s[r-3]==s[r-1]:
        cnt+=1
        
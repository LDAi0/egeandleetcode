f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 13/1.txt')
cnt=0
for line in f:
    a=[int(x) for x in line.split()]
    if len(a)==len(set(a)):
        if max(a)<(sum(a)-max(a)):
            cnt+=1
print(cnt)
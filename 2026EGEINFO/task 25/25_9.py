def find_M(n):
    D=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            D.add(i)
            D.add(n//i)
    if len(D)==0:
        return 0
    return min(D)+max(D)

cnt=0
res=[]
for i in range(700001, 10000000):
    if len(res)==5: 
        break
    if str(find_M(i))[-1]=='4':
        res.append([i,find_M(i)])

print(res)

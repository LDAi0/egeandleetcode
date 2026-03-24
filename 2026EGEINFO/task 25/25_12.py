def find_m(n):
    ans=set()
    for i in range(2,int(n**0.5)):
        if n%i==0:
            ans.add(i)
            ans.add(n//i)
    if len(ans)==0: return 0
    return min(ans)+max(ans)

cnt=0
print('govnno')

for i in range(800001,1000000):
    if cnt==5:break
    if str(find_m(i))[-1]=='4':
        print(i,find_m(i))
        cnt+=1

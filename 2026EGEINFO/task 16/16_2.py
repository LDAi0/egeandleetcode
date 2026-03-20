def f(n):
    if n==0:
        return 0
    elif n%2==0:
        return f(n/2)-1
    elif n%2!=0:
        return 1+f(n-1)
    else:
        print('error')

cnt=0
for n in range(0,1000):
    if f(n)==0:
        cnt+=1
print('dasd')
print(cnt)
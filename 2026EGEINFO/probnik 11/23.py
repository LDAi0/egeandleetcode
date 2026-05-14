def summa(n):
    res=n
    while n>0:
        res=res-(n%10)
        n//=10
    return res

def f(n,end):
    if n<end: return 0
    if n==end: return 1
    return f(n-4,end)+f(summa(n),end)

print('temp',f(36,14)*f(14,2))
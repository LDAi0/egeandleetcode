def uvel(n):
    if n%100>=90:
        return n
    return n+10

def f(n,end):
    if n>end: return 0
    if n==end: return 1
    return f(n+1,end)+f(uvel(n),end)
print('temp', f(10,33))
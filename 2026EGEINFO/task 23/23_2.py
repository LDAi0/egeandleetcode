from sys import setrecursionlimit

setrecursionlimit(1000)

def sum_numb(x):
    return sum(int(d) for d in str(x))

def f(n,end):
    if n>end: return 0
    if n==end: return 1
    return f(n+2,end)+f(n+sum_numb(n),end)
    
print('temp', f(3,29)*f(29,68))
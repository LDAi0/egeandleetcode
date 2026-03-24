from sys import setrecursionlimit

setrecursionlimit(100000)

def f(n,end,turn):
    if n>end: return 0
    if n==end: return 1 if (turn-1)%2!=0 else 0 
    if turn%2==0:
        return f(n+2,end,turn+1)
    return f(n+3,end,turn+1)+f(n+2,end,turn+1)+f(n*2,end,turn+1)

print('temp', f(1,50,1))
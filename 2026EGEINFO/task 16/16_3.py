from sys import setrecursionlimit

setrecursionlimit(100000)

def f(n):
    return g(n-1)+g(n-3)
def g(n):
    if n<=9:
        return 3*n
    return g(n-4)+2

print('tem', f(42999))
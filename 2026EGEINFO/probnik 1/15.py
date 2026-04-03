def dele(n,m):
    return n%m==0
def f(x,a):
    return ((dele(x,3)<=(not dele(x,2))) or (x-a>=4))

print('temp', max([a for a in range(1,10000000) if all(f(x,a)==1 for x in range(1,10000000))]))
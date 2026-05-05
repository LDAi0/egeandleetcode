def deli(n,m):
    return n%m==0
def f(x,a):
    return (deli(x,3)<=(not deli(x,2))) or (x-a>=4)
print(max([a for a in range(1,10000) if all(f(x,a)==1 for x in range(1,10000))]))
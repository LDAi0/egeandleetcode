def delet(x):
    return x//10
def f(n,end):
    if n<end: return 0
    if n==end: return 1
    ways=[f(n-3,end)]
    if n%2==0:
        ways.append(f(n//3,end))
    if n>9:
        ways.append(f(delet(n),end))
    return sum(ways)
print('temp', f(1250,20))
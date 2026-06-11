from string import printable
def f(n):
    r=''
    while n>0:
        r=printable[n%9]+r
        n//=9
    return r
res=[]
for x in range(1,2401):
    x1=7*9**210+6*9**110-x
    if f(x1).count('0')==100:
        res.append(x)
print(max(res))

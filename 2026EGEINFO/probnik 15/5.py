from string import printable
def per(x):
    res=''
    while x>0:
        res=printable[x%9]+res
        x//=9
    return res

m=[]
for n in range(1,100000):
    r=per(n)
    if r[0]=='7':
        r=r.replace('6','h')
        r=r.replace('3','6')
        r=r.replace('h','3')
        r='34'+r
    else:
        r='3'+r[1:]+'45'
    r=int(r,9)
    if r<2876:
        m.append([r,n])
print(max(m))
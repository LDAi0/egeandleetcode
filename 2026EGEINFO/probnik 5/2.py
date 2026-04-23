from itertools import product,permutations
def f(x,y,z):
    return (not(x==y<=z))
print('temp')
t=(
    (0,0,1,1),
    (0,1,1,0)
)
if len(t)==len(set(t)):
    for p in permutations('xyz',r=3):
        if all(f(**dict(zip(p,line)))==line[-1] for line in t):
            print(p)
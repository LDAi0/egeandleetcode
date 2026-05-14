from itertools import product,permutations

def f(x,y,z,w):
    return x or ((not y) or z or (not w)) and (y or (not z))

t=(
    (0,0,1,0,0),
    (1,0,0,1,0),
    (1,0,1,0,0)
)
for p in permutations('xyzw',r=4):
    if all(f(**dict(zip(p,line)))==line[-1] for line in t):
        print(*p)
from itertools import permutations,product

def f(x,y,z,w):
    return y and (x or z) or (not(y or z)) or w

for x1,x2,x3,x4 in product([0,1], repeat=4):
    t = (
        (1,x1,0,1,0),
        (x2,1,0,x3,0),
        (0,0,x4,1,0)
    )
    if len(t)==len(set(t)):
        for p in permutations('xyzw',r=4):
            if all(f(**dict(zip(p,line)))==line[-1] for line in t):
                print(*p)
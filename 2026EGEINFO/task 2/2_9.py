from itertools import product,permutations
def f(x,y,z,w):
    return (w==z) or (x and (not y)) or w
print('tmep')
for x1,x2,x3,x4,x5,x6,x7 in product([0,1],repeat=7):
    t=(
        (x1,x2,1,x3,0),
        (x4,0,x5,x6,0),
        (x7,1,0,0)
    )
    if len(t)==len(set(t)):
        for p in permutations('xywz',r=4):
            if all(f(**dict(zip(p,line)))==line[-1] for line in t):
                print(p)
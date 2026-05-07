from itertools import product

n = 1
res = []
for x in product("авнрья", repeat=5):
    a = "".join(x)
    if a[0] != "я" and a.count("ь") <= 1 and "яя" not in a:
        res.append(n)
    n += 1
print(max(res))

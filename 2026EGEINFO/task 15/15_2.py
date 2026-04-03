print('temp')
for a in range(1,1000):
    is_valid=True
    for x in range(1,1000):
        p=(x&103==0)and(x&94!=0)
        q=(x&a!=0)
        if not(not p or q):
            is_valid=False
            break
    if is_valid:
        print(a)
        break
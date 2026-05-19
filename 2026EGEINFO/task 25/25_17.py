import re
print('temp')
for x in range(253,10**8+1,253):
    if re.fullmatch(r'12\d\d15\d*6',str(x)) is not None:
        print(x,x//253)
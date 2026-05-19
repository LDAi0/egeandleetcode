import re
print('temp')
for x in range(2023,10**8+1,2023):
    if re.fullmatch(r'3[0123456789]1[0123456789]*57',str(x)) is not None:
        print(x,x//2023) 
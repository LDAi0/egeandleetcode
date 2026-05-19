import re
print('temp')
for x in range(237,10**8+1,237):
    if (re.fullmatch(r'81\d2\d*80',str(x)) is not None) and (re.fullmatch(r'\d*9\d*',str(x)) is None):
        print(x,x//237)
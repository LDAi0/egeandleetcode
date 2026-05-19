import re

print('temp')
for x in range(151,10**9+1,151):
    if re.fullmatch(r'2\d34\d56\d8',str(x)) is not None:
        print(x,x//151)
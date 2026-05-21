import re

for x in range(28,10**9+1,28):
    if re.fullmatch(r'6323\d*353\d',str(x)):
        print(x,x//28)
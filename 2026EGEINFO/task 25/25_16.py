import re 
def f(n):
    res=0
    while n>0:
        res+=n%10
        n//=10
    if res%7==0 and res<20:
        return True
    else: return False
print('temp')
for x in range(2023,10**9+1,2023):
    if (re.fullmatch(r'20\d*23',str(x)) is not None) and f(x):
        print(x)
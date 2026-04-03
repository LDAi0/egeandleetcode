def des(n,m):
    if n%m==0: return True
    else: return False
def sumbol(s,d):
    if s+d>0: return True
    else: return False
print('temp')

for x in range(1,160):
    if not(des(x,7)<= (not sumbol(x,-17))):
        print(x)

from re import *
s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_18619_A.txt').readline()
num=r'([123456]+)'
vyr=rf'({num}([-*]{num})*)'
p=rf'B{vyr}'

m=max([x.group() for x in finditer(p,s)],key=len)
print(len(m))
print(m)

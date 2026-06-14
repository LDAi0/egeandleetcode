from re import *
s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_17641_A.txt').readline()
num=r'(([1-9][0-9]*)|0)'
pr=rf'(({num}\*)*0(\*{num})*)'
p=rf'{pr}(\+{pr})*'
m= max([x.group() for x in finditer(p,s)], key=len)
print(len(m),m)


from re import *
s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_17756_A.txt').readline()
num=r'([0-9]+)'
p=rf'[+*]?{num}([+*]{num})*[+*]?'

print(max([len(x.group()) for x in finditer(p,s)]))


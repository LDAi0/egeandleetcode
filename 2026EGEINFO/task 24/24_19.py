from re import *
s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_17563_A.txt').readline()

num=r'([789][0789]*)'
p=rf'{num}([-*]{num})+'
print(s[:100])
print(max([len(x.group()) for x in finditer(p,s)]))
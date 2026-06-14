from re import *
s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_17563_A.txt').readline()

p=r'([789][0789]*)([-*][789][0789]*)*'
print(s[:100])
print(max([len(x.group()) for x in finditer(p,s)]))

temp='ABACBACACACBBBC'
for x in ['ABA','CB','AC','BB','ABC','BCB','BA','AB']: temp=temp.replace(x,'1')
print(temp)
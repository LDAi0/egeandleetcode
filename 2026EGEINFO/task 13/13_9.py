from ipaddress import ip_network
res=[]
ip='76.155.48.2'
cnt=0
for mask in range(16,33):
    net=ip_network(f'{ip}/{mask}',0)
    if str(net.network_address) == '76.155.48.0':
        cnt+=1
print('tmep',cnt)
print(net.network_address)

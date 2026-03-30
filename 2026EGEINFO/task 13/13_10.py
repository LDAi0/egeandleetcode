from ipaddress import ip_network
cnt=0
mask='255.255.255.128'

net=ip_network(f'0.0.0.0/{mask}',0)
for ip in net:
    cnt+=1
print('temp',cnt)
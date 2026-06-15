from ipaddress import ip_network
m=[]
for mask1 in range(1,33):
    for mask2 in range(1,33):
        net1=ip_network(f'157.127.182.76/{mask1}',0)
        net2=ip_network(f'157.127.190.80/{mask2}',0)
        if bin(int(net1.netmask))[2:].count('1')==bin(int(net1.netmask))[2:].count('1') and net1!=net2:
            m.append(bin(int(net1.netmask))[2:].count('1'))
    print(bin(int(net1.netmask))[2:])   
print('temp',min(m))
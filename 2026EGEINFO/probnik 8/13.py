from ipaddress import ip_network
for m in range(0,33):
    net=ip_network(f'145.192.94.230/{m}',0)
    if str(net.network_address)=='145.192.80.0':
        print(str(net.netmask))
        
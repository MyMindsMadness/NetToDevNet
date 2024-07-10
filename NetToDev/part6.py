# MyMindsMadness
# Storing the config

int_config = []
intf = "interface vlan"
vlan = 10
ip = " ip address"
ms = "255.255.255.0"
a = 192
b = 168
for c in range(10 , 81 , 10):
    d = 5
    int_config.append(f"{intf} {vlan}")
    int_config.append(f"{ip} {a}.{b}.{c}.{d} {ms}")
    vlan += 10

print (int_config)
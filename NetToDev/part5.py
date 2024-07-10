# MyMindsMadness
# Better IPScheme
intf = "interface vlan"
vlan = 10
ip = " ip address"
ms = "255.255.255.0"
a = 192
b = 168
for c in range(10 , 81 , 10):
    d = 5
    print (f"{intf} {vlan}")
    print (f"{ip} {a}.{b}.{c}.{d} {ms}")
    vlan += 10
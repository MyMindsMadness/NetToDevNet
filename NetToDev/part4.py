# MyMindsMadness
# Print as Config

intf = "interface vlan"
vlan = 2
ip = " ip address"
ms = "255.255.255.0"
a = 192
b = 168
for c in range(256):
    d = 5
    print (intf, vlan)
    print (f"{ip} {a}.{b}.{c}.{d} {ms}")
    vlan += 2
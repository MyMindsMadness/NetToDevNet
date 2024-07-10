# MyMindsMadness
# Send your config
# to to device

# issue command "pip install scapli"

from scrapli.driver.core import IOSXEDriver

dev8k = {
    'host':'10.10.20.48',
    'auth_username':'developer',
    'auth_password':'C1sco12345',
    'auth_strict_key':False
}

conn = IOSXEDriver(**dev8k)
conn.open()
response = conn.send_command("show ip int br")
print (response)
print (response.result)

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
sendconf = conn.send_commands(int_config)
response2 = conn.send_command("show ip int br")
print (response2.result)
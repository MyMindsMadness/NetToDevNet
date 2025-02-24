import random 

def dhcp():
    select = random.randint(0, 255)
    return (f"IP : 192.168.0.{select}")

print (dhcp())
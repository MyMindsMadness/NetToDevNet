# Let's Create a script that Simulates DHCP
import random

leased_addresses = []

def dhcp(leased):
    network="192.168.0."
    for i in range (30):
        host = random.randint(10,20)
        address = f"{network}{str(host)}"
        if address in leased:
            print (f"{address} is in use")
        else:
            leased.append(address)
            print (f"Your address is {address}")

def main():
    dhcp(leased_addresses)
    print (sorted(leased_addresses))

main()
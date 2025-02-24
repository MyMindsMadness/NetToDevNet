# Let's Create a script that Simulates DHCP
import random
import time 
import json

leased_addresses = {}

def dhcp(leased):
    network="192.168.0."
    for i in range (10):
        time.sleep(1)
        host = random.randint(10,20)
        address = f"{network}{str(host)}"
        if address in leased:
            print (f"{address} is in use")
        else:
            st, et, ed = lease_time()
            leased[address] = {"address": address, 
                               "leased_time": st, 
                               "expiry_time": et, 
                               "expiry_date": ed}
            print (f"\nYour address is {address}\n") 
            lease_expiry(leased)
        
def lease_time():
    start = time.time()
    expiry = start + 5
    start_time_str = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(start))
    expiry_time_str = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(expiry))
    return start_time_str, expiry, expiry_time_str
       
def lease_expiry(leased_addr):
    current_time = time.time()
    for address in list(leased_addr.keys()):
        if leased_addr[address]["expiry_time"] < current_time:
            print (f"\nAddress {address} has expired\n")
            del leased_addr[address]
    print ("***Leased Addresses***")
    print (json.dumps(leased_addr, indent=2))
    print ("***End of Leased Addresses***\n")

def main ():
    dhcp(leased_addresses)
    
if __name__ == "__main__":
    main()
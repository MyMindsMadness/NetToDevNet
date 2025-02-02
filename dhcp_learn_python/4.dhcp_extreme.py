import random
import json
import time

vlan10={}
vlan20={}
vlan30={}
expired_leases={}

Test_data = {"request1":  {"vlan": 10, "mac": "00:11:22:33:44:55"},
             "request2":  {"vlan": 20, "mac": "00:11:22:33:44:56"},
             "request3":  {"vlan": 30, "mac": "00:11:22:33:44:57"},
             "request4":  {"vlan": 10, "mac": "00:11:22:33:44:58"},
             "request5":  {"vlan": 20, "mac": "00:11:22:33:44:59"},
             "request6":  {"vlan": 30, "mac": "00:11:22:33:44:60"},
             "request7":  {"vlan": 10, "mac": "00:11:22:33:44:61"},
             "request8":  {"vlan": 20, "mac": "00:11:22:33:44:62"},
             "request9":  {"vlan": 30, "mac": "00:11:22:33:44:63"},
             "request10": {"vlan": 10, "mac": "00:11:22:33:44:64"},
             "request11": {"vlan": 20, "mac": "00:11:22:33:44:65"},
             "request12": {"vlan": 30, "mac": "00:11:22:33:44:66"},
             "request13": {"vlan": 10, "mac": "00:11:22:33:44:67"},
             "request14": {"vlan": 20, "mac": "00:11:22:33:44:68"},
             "request15": {"vlan": 30, "mac": "00:11:22:33:44:69"},
             "request16": {"vlan": 10, "mac": "00:11:22:33:44:70"},
             "request17": {"vlan": 20, "mac": "00:11:22:33:44:71"},
             "request18": {"vlan": 30, "mac": "00:11:22:33:44:72"},
             "request19": {"vlan": 10, "mac": "00:11:22:33:44:73"},
             "request20": {"vlan": 20, "mac": "00:11:22:33:44:74"},
             "request21": {"vlan": 30, "mac": "00:11:22:33:44:75"},
             "request22": {"vlan": 10, "mac": "00:11:22:33:44:76"},
             "request23": {"vlan": 20, "mac": "00:11:22:33:44:77"},
             "request24": {"vlan": 30, "mac": "00:11:22:33:44:78"},
             "request25": {"vlan": 10, "mac": "00:11:22:33:44:79"},
             "request26": {"vlan": 20, "mac": "00:11:22:33:44:80"},
             "request27": {"vlan": 30, "mac": "00:11:22:33:44:81"},
             "request28": {"vlan": 10, "mac": "00:11:22:33:44:82"},
             "request29": {"vlan": 20, "mac": "00:11:22:33:44:83"},
             "request30": {"vlan": 30, "mac": "00:11:22:33:44:84"},
             "request31": {"vlan": 10, "mac": "00:11:22:33:44:85"},
             "request32": {"vlan": 20, "mac": "00:11:22:33:44:86"},
             "request33": {"vlan": 30, "mac": "00:11:22:33:44:87"},
             "request34": {"vlan": 10, "mac": "00:11:22:33:44:88"},
             "request35": {"vlan": 20, "mac": "00:11:22:33:44:89"},
             "request36": {"vlan": 30, "mac": "00:11:22:33:44:90"},
             "request37": {"vlan": 10, "mac": "00:11:22:33:44:91"},
             "request38": {"vlan": 20, "mac": "00:11:22:33:44:92"},
             "request39": {"vlan": 30, "mac": "00:11:22:33:44:93"},
             "request40": {"vlan": 10, "mac": "00:11:22:33:44:94"},
             "request41": {"vlan": 20, "mac": "00:11:22:33:44:95"},
             "request42": {"vlan": 30, "mac": "00:11:22:33:44:96"},
             "request43": {"vlan": 10, "mac": "00:11:22:33:44:97"},
             "request44": {"vlan": 20, "mac": "00:11:22:33:44:98"},
             "request45": {"vlan": 30, "mac": "00:11:22:33:44:99"},
             "request46": {"vlan": 10, "mac": "00:11:22:33:44:a0"},
             "request47": {"vlan": 20, "mac": "00:11:22:33:44:a1"},
             "request48": {"vlan": 30, "mac": "00:11:22:33:44:a2"},
             "request49": {"vlan": 10, "mac": "00:11:22:33:44:a3"},
             "request50": {"vlan": 20, "mac": "00:11:22:33:44:a4"}
            }

def dhcp(vlan, mac):
    net_space = f"vlan{vlan}"
    network = f"192.168.{vlan}."
    while True:
        host = random.randint(10, 100)
        address = f"{network}{str(host)}"
        if net_space == "vlan10":
            if address not in vlan10:
                db_builder(vlan10, address, mac)
                print (f"Address {address} assigned to {mac}")
                lease_expiry(vlan10)
                break
            else:
                print (f"Address {address} is in use")
        elif net_space == "vlan20":
            if address not in vlan20:
                db_builder(vlan20, address, mac)
                print (f"Address {address} assigned to {mac}")
                lease_expiry(vlan20)
                break
            else:
                print (f"Address {address} is in use")
        elif net_space == "vlan30":
            if address not in vlan30:
                db_builder(vlan30, address, mac)
                print (f"Address {address} assigned to {mac}")
                lease_expiry(vlan30)
                break
            else:
                print (f"Address {address} is in use")

def lease_time():
    start = time.time()
    expiry = start + 4
    start_time_str = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(start))
    expiry_time_str = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(expiry))
    return start_time_str, expiry, expiry_time_str

def db_builder(leased, address, mac):
    net = address.split(".")[:-1]
    gateway = ".".join(net) + ".1"
    st, et, ed = lease_time()
    leased[address] = {"address": address,
                       "subnet mask": "255.255.255.0",
                       "gateway": gateway,
                       "physical_address": mac,
                       "leased_time": st, 
                       "expiry_time": et, 
                       "expiry_date": ed}

def lease_expiry(leased_addr):
    current_time = time.time()
    for address in list(leased_addr.keys()):
        if leased_addr[address]["expiry_time"] < current_time:
            print (f"""\nAddress {address} has expired
                   Removing {address} from the database\n""")
            expired_leases[address] = leased_addr[address]
            del leased_addr[address]

def main():
    for request in Test_data:
        time.sleep(0.10)
        vlan = Test_data[request]["vlan"]
        mac = Test_data[request]["mac"]
        dhcp(vlan, mac)
    print ("***PRINTING VLAN 10 DATABASE***")
    sorted_vlan10 = {k: vlan10[k] for k in sorted(vlan10)}
    output = json.dumps(sorted_vlan10,indent=2)
    with open("dhcp_learn_python/output/vlan10.json", "w") as file:
        file.write(output)
    print ("***PRINTING VLAN 20 DATABASE***")
    sorted_vlan20 = {k: vlan20[k] for k in sorted(vlan20)}
    output = json.dumps(sorted_vlan20,indent=2)
    with open("dhcp_learn_python/output/vlan20.json", "w") as file:
        file.write(output)
    print ("***PRINTING VLAN 30 DATABASE***")
    sorted_vlan30 = {k: vlan30[k] for k in sorted(vlan30)}
    output = json.dumps(sorted_vlan30,indent=2)
    with open("dhcp_learn_python/output/vlan30.json", "w") as file:
        file.write(output)
    print ("***PRINTING EXPIRED LEASES DATABASE***")
    sorted_expired_leases = {k: expired_leases[k] for k in sorted(expired_leases)}
    output = json.dumps(sorted_expired_leases,indent=2)
    with open("dhcp_learn_python/output/expired_leases.json", "w") as file:
        file.write(output)

if __name__ == "__main__":
    main() 
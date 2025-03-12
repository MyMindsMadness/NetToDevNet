from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import inquirer as inq
import ipaddress
import random
import string

# global variables
config = []

# helper functions
def range_selector(low, high, user_message):
    num_list = list (range(low, high))
    number_strings = [str(num) for num in num_list]
    num_completer = WordCompleter(number_strings, ignore_case=True)
    while True:
        user_input = prompt(user_message, completer=num_completer)
        if user_input.isdigit() and int(user_input) in num_list:
            return user_input
        else:
            print ("Outside of accepted range, Please try again!")

def select_from_list(custom_list, custom_message):
    selector = [
        inq.List(
            'selection',
            message=custom_message,
            choices=custom_list,
            carousel=True,)
    ]
    answer = inq.prompt(selector)
    return (answer['selection'])

def yes_no_button(message):
    yes_no_button = ["Yes", "No"]
    configure = select_from_list(yes_no_button, message)
    if configure == "Yes":
        return True
    else:
        return False

def interface_ip(message):
    while True:
        user_input = input(message)
        try:
            # Check if the input is a valid IPv4 address
            ipaddress.IPv4Address(user_input)
            return user_input
        except ipaddress.AddressValueError:
            print("Invalid IPv4 address. Please try again.")

def secret():
    rgen = yes_no_button("Would you like a randomly generated Pre-Shared key? ")
    if rgen == True:
        characters = string.ascii_letters + string.digits + string.punctuation
        preshared = ''.join(random.choice(characters) for _ in range(20))

    else:
        preshared = input("Enter a Pre-Shared Key: ")
    return preshared

def subnet_mask():
    subnet_masks = [
    "255.255.255.0", # /24
    "255.255.255.128", # /25
    "255.255.255.192", # /26
    "255.255.255.224", # /27
    "255.255.255.240", # /28
    "255.255.255.248", # /29
    "255.255.255.252", # /30
    "255.255.255.254", # /31
    "255.255.255.255"  # /32
    ]
    return select_from_list(subnet_masks, "Select a subnetMask: ")   

# main body functions
def outside_interface():
    method_option = ["GigabitEthernet0/0", 
                     "GigabitEthernet0/1",
                     "GigabitEthernet0/2",
                     "GigabitEthernet0/3"]
    if yes_no_button("Would you like to configure OUTSIDE interface? ") == True:
        outside_message = "Select Outside Interface"
        selected_method = select_from_list(method_option, outside_message)
        config.extend([f"interface {selected_method}",
                       "nameif outside",
                       f" ip address {interface_ip("Please Enter IP Address: ")} {subnet_mask()}",
                       f" security-level {security_level()}",
                       " no shutdown",
                       "!"])
        if selected_method in method_option:
            method_option.remove(selected_method)
    if yes_no_button("Would you like to configure INSIDE interface? ") == True:
        inside_interface(method_option)

def inside_interface(available_interfaces):
    inside_message = "Select Inside Interface"
    selected_method = select_from_list(available_interfaces, inside_message)
    config.extend([f"interface {selected_method}",
                   "nameif inside",
                   f" ip address {interface_ip("Please Enter IP Address: ")} {subnet_mask()}",
                   f" security-level {security_level()}",
                   " no shutdown",
                   "!"])

def security_level():
    low = 0
    high = 101
    message = "Enter a Security Level: "
    return (range_selector(low, high, message))

def crypto_policy():
    low = 1
    high = 65537
    message = "Enter a Policy Number: "
    config.append(f"crypto isakmp policy {range_selector(low,high,message)}")

def authentication_method():
    method_option = ["pre-share", "rsa-sig"]
    message = "Select Authentication Method"
    selected_method = select_from_list(method_option, message)
    config.append(f" authentication {selected_method}")

def encryption_algorithm():
    algorithms = ["des", "3des", "aes", "aes-192", "aes-256"]
    message = "Select Encryption Algorithm"
    selected_algo = select_from_list(algorithms, message)
    config.append(f' encryption {selected_algo}')

def hashing_algorithm():
    algorithms = ["md5", "sha", "sha256", "sha384", "sha512"]  
    message = "Select Hashing Algorithm"
    selected_algo = select_from_list(algorithms, message)
    config.append(f' hash {selected_algo}')  

def group_value():
    algorithms = ["Group 1 : 768-bit modulus (weak, not recommended)",
                  "Group 2 : 1024-bit modulus (moderate security)",
                  "Group 5 : 1536-bit modulus",
                  "Group 14: 2048-bit modulus (strong security)",
                  "Group 19: ",
                  "Group 20: ",
                  "Group 21:"]  
    message = "Select Diffie-Helman (DH) Group"
    selected_algo = select_from_list(algorithms, message)
    config.append(f' {selected_algo.split(":")[0].strip().lower()}')

def lifetime():
    low = 60
    high = 86401
    message = "Please Enter a lifetime value: "
    config.extend([f' lifetime {range_selector(low, high, message)}',"!"])
    
def enable_ikev_outside():
    config.extend([" crypto ikev1 enable outside","!"])

def tunnel_group():
    address = interface_ip("Please Enter Tunnel ID (in IP Address format): ")
    config.extend([f"tunnel-group {address} type ipsec-l2l",
                  f"tunnel-group {address} ipsec-attributes",
                  f"ikev1 pre-shared-key {secret()}",
                  "!"])

def og_creator(groupname):
    config.append(f"object-group network {groupname}")
    while True:
        config.append(f" network-object {interface_ip(f"Add {groupname} Network address(es): ")} {subnet_mask()}")
        if not yes_no_button("Would you like to add another network?"):
            break

def network_og():
    og_creator("local-network")
    og_creator("remote-network")  
    config.append("!")

def interesting_traffic(local, remote):
    config.append(f"access-list asa-router-vpn extended permit ip object-group {local} object-group {remote}")

def net():
    config.append("nat (inside,outside) source static local-network local-network destination static remote-network remote-network no-proxy-arp route-lookup")
    config.append("!")

def cryptmap():
    map = range_selector(1, 65546, "Enter Crypto Map Value: ")
    peer_ip = interface_ip("VPN Peer Address: ")
    config.extend([
        f"crypto map outside_map {map} match address asa-router-vpn",
        f"crypto map outside_map {map} set peer {peer_ip}",
        f"crypto map outside_map {map} set ikev1 transform-set ESP-AES256-SHA",
        "crypto map outside_map interface outside",
        "!"
    ])

def main():
    outside_interface()
    crypto_policy()
    authentication_method()
    encryption_algorithm()
    hashing_algorithm()
    group_value()
    lifetime()
    enable_ikev_outside()
    tunnel_group()
    network_og()
    interesting_traffic("local-network","remote-network")
    cryptmap()

    print ("\n", '*' * 40)
    print ("Here is the ASA config")
    print ('*' * 40, "\n")
    for conf_line in config:
        print (conf_line)

if __name__ == "__main__":
    main()
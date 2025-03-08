from ntc_templates.parse import parse_output
from netmiko import ConnectHandler
import json

def backup_config(device_name, net_connect):
    output = net_connect.send_command('show running-config')
    with open (f'backup/{device_name}.txt', 'w') as backup:
        backup.write(output)

def logon():
    # Define the device details
    with open ('devices.json') as f:
        device_list = json.load(f)
    # Establish an SSH connection to the device
    for device in device_list:
        device_name = device['host']
        print (f"\nConnecting to: {device_name} \n")
        net_connect = ConnectHandler(**device)
        # Enter enable mode (if necessary)
        net_connect.enable()
        backup_config(device_name, net_connect)
        # Send the 'show ip int brief' command
        output = net_connect.send_command(
            'show ip int brief')
        # Parse the interface output
        interfaces_parsed = parse_output(
            platform="cisco_ios", 
            command="show ip interface brief", 
            data= output)
        int_config(
            net_connect, 
            interfaces_parsed,
            device_name)
        net_connect.disconnect()

def int_config(net_connect, interfaces_parsed, dev_name):
    int_list = []
    for interface in interfaces_parsed:
        gint= interface["interface"]
        command = f"show run interface {gint}"
        output = net_connect.send_command(command)
        # SEARCH STRING - change to match your requirements
        if "authentication order dot1x mab" in output:
            print(f'Interface {gint}: \033[31mReconfiguration required\033[m')
            # Add interface to list for audit log of interfaces requiring reconfiguration
            int_list.append(f'Interface {gint}: Reconfiguration required\n')
        else:
            print (f'Interface {gint}: \033[34mConfiguration Not Required\033[m')
    int_out(int_list, dev_name)

def int_out(int_list, dev_name):
    # Create audit log of interfaces requiring reconfiguration
    with open (f'reconn/{dev_name}.txt', 'w') as f:
        for item in int_list:
            f.write(item)

logon()
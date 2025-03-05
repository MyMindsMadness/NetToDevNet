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
            interfaces_parsed)
        net_connect.disconnect()

def int_config(net_connect, interfaces_parsed):
    for interface in interfaces_parsed:
        gint= interface["interface"]
        command = f"show run interface {gint}"
        output = net_connect.send_command(command)
        # SEARCH STRING - change to match your requirements
        if "authentication order dot1x mab" in output:
            print (
                f'Interface {gint}: \033[31mReconfiguration required\033[m')
            # Define the commands to reconfigure the interface
            commands = [
                f'interface {gint}', 
                'authentication order mab dot1x']
            # Send the configuration commands to the device
            reconf = net_connect.send_config_set(
                commands)
            # Print the configuration changes
            for line in reconf.splitlines():
                if "(config" in line:
                    print (f'\t{line}')
                    
        # If the interface is already configured correctly ignore
        else:
            print (
                f'Interface {gint}: \033[34mConfiguration Not Required\033[m')    

logon()
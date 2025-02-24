import time
user_exec  = "R1>"
priv_exec = "R1#"
config_terminal = "R1(config)#"
config_interface = "R1(config-if)# "

def interface(module, intf):
    line = (f"interface GigabitEthernet{module}/{intf}")
    return line

def no_shut():
    return (f" no shutdown")

def ip_address(x):
    line = (f" ip address 192.168.{x}.1 255.255.255.0")
    return line
    
def priv_exec_mode():
    print_with_delay (f"{user_exec} enable")
    for i in range(3):
        print_with_delay (f"{priv_exec}")
    config_terminal_mode()

def config_terminal_mode():
    print_with_delay (f"{priv_exec} conf t")

def config_spacing():
    for i in range(3):
        print_with_delay (f"{config_terminal}")

def interface_config():
    x = 1
    priv_exec_mode()
    for i in range(1, 3):
        for j in range(1,3):
            address = ip_address(x)
            print_with_delay (f"{config_interface}{interface(i, j)}")
            print_with_delay (f"{config_interface}{description(address)}")
            print_with_delay (f"{config_interface}{address}")
            print_with_delay (f"{config_interface}{no_shut()}")
            print_with_delay (f"{config_interface} exit")
            print_with_delay (f"{config_terminal}")
            config_spacing()
            x+=1

def description(address):
    return (f" description {address}")

def show_run():
    x =1
    print_with_delay (f"{priv_exec} show run interface")
    print_with_delay ("!")
    for i in range(1, 3):
        for j in range(1,3):
            address = ip_address(x)
            x+=1
            print_with_delay (f"{interface(i, j)}")
            print_with_delay (f"{description(address)}")
            print_with_delay (f"{address}")
            print_with_delay (f"{no_shut()}")
            print_with_delay ("!")

def end():
    print_with_delay (f"{config_terminal} end")
    print_with_delay (f"{priv_exec}")

def print_with_delay(message, delay=0.2):
    print (message)
    time.sleep(delay)

def main ():
    interface_config()
    end()
    show_run()

if __name__ == "__main__":
    main()
    


### Creating ClassA function ###
def ClassA():
    octet1 = 10
    for octet2 in range (256):
        for octet3 in range(256):
            for octet4 in range (256):
                print (f"{octet1}.{octet2}.{octet3}.{octet4}")

### Creating ClassB function ###
def ClassB():
    ### Setting static Values ###
    octet1 = 172
    ### Creating a range loop for octet2 ###
    for octet2 in range (16,32):
        for octet3 in range(256):
            octet4 = 0
        ### Create a while loop that prints IP and adds 1 to octet3 ###
            while octet4 < 256:
                print (f"{octet1}.{octet2}.{octet3}.0")
                octet4 += 1

### Creating ClassC function ###
def ClassC():
    ### Setting static Values ###
    octet1 = 192
    octet2 = 168
    ###Creating a range loop for octet3 ###
    for octet3 in range (256):
        octet4 = 0
        ### Create a while loop that prints IP and add1 to octet4 ###
        while octet4 < 256:
            print (f"{octet1}.{octet2}.{octet3}.{octet4}")
            octet4 += 1

### Call function to run in script ###
ClassC()
ClassB()
ClassA()
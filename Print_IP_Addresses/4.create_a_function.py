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
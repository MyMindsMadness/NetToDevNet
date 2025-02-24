### Setting static Values ###
octet1 = 192
octet2 = 168
octet3 = 0
octet4 = 0

### Create a while loop that prints IP and adds 1 to octet4 ###
while octet4 < 256:
    print (f"{octet1}.{octet2}.{octet3}.{octet4}")
    octet4 += 1
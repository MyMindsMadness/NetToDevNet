def part1():
    octet1 = 192
    octet2 = 168
    octet3 = 0
    octet4 = 0
    print (octet1, "." , octet2, "." , octet3 , "." , octet4  )

def part2():
    octet1 = 192
    octet2 = 168
    octet3 = 0
    octet4 = 0
    while octet4 < 256:
        print (f"{octet1}.{octet2}.{octet3}.{octet4}")
        octet4 +=1

def part3():
    octet1 = 192
    octet2 = 168
    for octet3 in range (256):
        octet4=0
        while octet4 < 256:
            print (f"{octet1}.{octet2}.{octet3}.{octet4}")
            octet4 +=1

def ClassC():
    octet1 = 192
    octet2 = 168
    for octet3 in range(256):
        for octet4 in range(256):  
            print (f"{octet1}.{octet2}.{octet3}.{octet4}")

def ClassB():
    octet1 = 172
    for octet2 in range (16,32):
        for octet3 in range(256):
            for octet4 in range(256):  
                print (f"{octet1}.{octet2}.{octet3}.{octet4}")     

def ClassA():
    octet1 = 10
    for octet2 in range (256):
        for octet3 in range(256):
            for octet4 in range(256):  
                print (f"{octet1}.{octet2}.{octet3}.{octet4}")   

def AllIPv4():
    for octet1 in range (256):
        for octet2 in range (256):
            for octet3 in range(256):
                for octet4 in range (256):
                    print(f"{octet1}.{octet2}.{octet3}.{octet4}")

def switchIP():
    vlan = 2
    octet1 = 192
    octet2 = 168
    for octet3 in range(256):
        octet4 = 5
        print ("\n")
        print(f"interface vlan {vlan}")
        print (f" ip address {octet1}.{octet2}.{octet3}.{octet4} 255.255.255.0")
        vlan +=2  


### Remove the Hash to run each function. 
### Part1 is ready to run.  

part1()
#part2()
#part3()
#ClassC()
#ClassB()
#ClassA()
#AllIPv4()
#switchIP()
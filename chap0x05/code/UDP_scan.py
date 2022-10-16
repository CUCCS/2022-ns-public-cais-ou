from scapy.all import *

dst_ip="172.16.111.127"
dst_port= 53
pkts = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=10)
if pkts is None:
        print("Open or Filtered")
elif(pkts.haslayer(UDP)): 
        print("Open")
elif(pkts.haslayer(ICMP)):
        if(int(pkts.getlayer(ICMP).type) == 3 and int(pkts.getlayer(ICMP).code) in [1,2,9,10,13]):  
            print("Filtered")
        elif(int(pkts.getlayer(ICMP).type) == 3 and int(pkts.getlayer(ICMP).code) == 3):
            print("Closed")
        elif(pkts.haslayer(IP) and pkts.getlayer(IP).proto == IP_PROTOS.udp):
            print("Open")
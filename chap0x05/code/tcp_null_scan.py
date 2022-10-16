from scapy.all import *

dst_ip="172.16.111.127"
dst_port= 80
pkts = sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags=""),timeout=10)
if pkts is None:
        print("Open or Filtered")
elif(pkts.haslayer(TCP)):
        if (pkts.getlayer(TCP).flags == 0x14): 
         print("Closed")

elif(pkts.haslayer(ICMP)):
        if(int(pkts.getlayer(ICMP).type) == 3 and int(pkts.getlayer(ICMP).code in [1,2,3,9,10,13])):  
         print("Filtered")
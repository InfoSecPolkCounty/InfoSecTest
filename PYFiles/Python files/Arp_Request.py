#!/usr/bin/env python3
import netifaces
import scapy.all as scapy
import os, subprocess, getpass
from time import sleep

"""Need to convert to python3 for windows"""
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
    print(bcolors.FAIL + "Ip forward stopping" + bcolors.ENDC)
    ip_forward = "echo 0 > /proc/sys/net/ipv4/ip_forward"
    root_password = getpass.getpass("Enter Sudo password : ")
    subprocess.call('echo {} | sudo -S {}'.format(root_password, ip_forward), shell=True)
    print(bcolors.FAIL + "Ip forwarding halted" + bcolors.ENDC)


def start_forwarding_linux():
    ip_forward = "echo 1 > /proc/sys/net/ipv4/ip_forward"
    root_password = getpass.getpass("Enter Sudo password : ")
    print(bcolors.OKGREEN + "Forwarding Ip" + bcolors.ENDC)
    subprocess.call('echo {} | sudo -S {}'.format(root_password, ip_forward), shell=True)


def get_default_gateway_linux():
    if os.name == 'posix':
        print(bcolors.OKBLUE + "[+] Linux Detected grabbing default gateway" + bcolors.ENDC)
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        print(bcolors.OKBLUE + "Default Gateway is \n> " + default_gateway + bcolors.ENDC)
        return default_gateway
        sleep(10)
    else:
        print(bcolors.WARNING + "Not running linux" + bcolors.ENDC)
        pass


def get_default_gateway_windows():
    if os.name == 'nt':
        print(bcolors.OKBLUE + "[+] Windows Detected grabbing default gateway" + bcolors.ENDC)
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        print(bcolors.OKBLUE + "Default Gateway is\n> " + default_gateway + bcolors.ENDC)
        return default_gateway
    else:
        print(bcolors.WARNING + "Not Running Windows" + bcolors.ENDC)
        pass


def scan(default_gateway):
    arp_request = scapy.ARP(pdst=default_gateway)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("\n IP\t\t\t MAC\n" + "|" + "=" * 41 + "|")
    for client in results_list:
        print("|" + client["ip"] + "\t|\t" + client["mac"] + " |")
    print("|" + "=" * 41 + "|\n")


if os.name == 'nt':
    ip = get_default_gateway_windows()
    default_gateway = ip.__str__ + "/24"
elif os.name == 'posix':
    ip = get_default_gateway_linux()
    default_gateway = ip.__str__() + "/24"


try:
    while True:
        scan_result = scan(default_gateway)
        print_result(scan_result)
        sleep(5)
        subprocess.call("clear")
except KeyboardInterrupt:
    subprocess.call("clear")
    print_result(scan_result)
    banner = "\n" + bcolors.OKBLUE + """ 
                                             ,▄▄▄                              
                                           ▄▓█▀▀▀▀▀█▄                           
                   ▄▄▓█`       ,▄▄▓▓▄▄▄▄▄@██▀!√√√√√└▀█▄                         
                .▓█▀██       #█▀▀└:.!╙▀▀██▀:√√√√√√√√√!▀▀█▓▓▄▄                   
               ╓█▀..▀█▓▄▄▄▄▓▀▀:√√√√√√√√√√√√√√√√√√√√√√√√√░░▀▀██▄                 
               ██.√√√!▀▀▀▀▀:√√√√√√√√√√√√√√√√√√√√√√√√√√√√╠░░░░▀█▄                
               █▌√√√√√√√√√√√√√▄▄▄▄▄.√√√√√√√╓▄▄▄.√√√√√√√√╠░░░░░╙█▄               
               ██.√√√√√√√√√▄#█▀╙`╙▀█▓▄▄▄@▓██████▄.√√√√√╠░░░░░░░╙█▓▄             
             ┌████:√√√√√(▄█▀╙       └▀▀▀▀└   └▀▀██,√√╓╢░░░░░░░░░░▀██▄           
             ██:√╙▀▓▄▄▓▓▀▀                      └██▄░░░░░░░░░░░░░░░██▄          
             █▌√√╓██▀  ▄▄@╕                       ▀▀█▓▀▀▀▀▀▀███▄░░░░██▄         
             ██▄▓█▀  ╙▀▀▀▀▀                 ,▄               ▀███░░░░██▄        
              ███`                         ▓███,     .        ███░░░░║██        
             ▓█▀     ,▄                     └▀██▄            ▄██▀░░░░░██`       
            ██▀     ███¼        ,              ▀▀        ╓@██▀▀░░░░░░░██        
           ██▀     ▐███       ╓█▀        ▄▄,          .  ▄╙▀█░░░░░░░░╟██        
          ▐█▌       ▀▀└     .▓█└        #███          .  ╙█▓,▀█░░░░░░██▌        
          ██              ▄▓█▀          ███▌          . .▄,▀█▄╙█░░░░███         
         ╟█▌            #██▀            ╙▀▀           .  ▀█▓,█▄╙█░░███          
         ██─            ███                             ▓▄,▀█▄█,█░███`          
         ██             ╙███                         .   ▀█▄╙█Ö█████            
         ██    ,#         ╙╙                         . ╙█▄ ▀ ╙████▀             
         ██  ╒███▄▄                  ▐█▄            .   ╙▀  .@███┘              
         ██▌  ██▄ └╙▀▀#╦▄▄▄▄▄▄▄▄▄▄▄▄#████▄         .         ╙███               
         ▐██   ▀ ▀▓▄,     `└╙└└ .      ███▌        .          ╟██               
          ██▌      ╙▀█▓▄▄▄,   .,▄▄▄▓▓▀▀╙██        .          .███               
          └██▄        └▀▀▀███▀▀▀▀╙"     ▀       ..          ▄███                
           ╙██▄       Ñ▓▓▓▓µ                   ..    ▄▓▓▓▓███▀`                 
            └██▄        `└└                  ..    ▄███▀└└                      
              ▀██▄                          .   ▄▓██▀└                          
                ▀█▓▄                     ..  ▄▓██▀╙                             
                  ╙▀█▄,                .╓▄▓██████                               
                     ╙██▓▄         ...   '' ▄██▀                                
                      ╙█████▓▓▄▄▄▄      .▄▄██▀'                                 
                        ▀█████▄▄▄▄▄▄▄▄▓████▀                                    
                           ╙▀▀▀██████▀▀▀╙           """ + bcolors.ENDC
    print(bcolors.FAIL + "\nExiting" + bcolors.ENDC)
    print(banner)

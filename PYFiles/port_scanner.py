import socket
import sys




def portScan(host,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.1)
    if s.connect_ex((host,int(port))):
        pass
    else:
        print(f"\n[+] Port " + str(port) + " is open on " + str(host) + "\n",end='',flush=True)
        try:
            banner_grab(host,port)
        except socket.timeout:
            print("Unable to grab banner from: " + str(host) + ":" + str(port))


def banner_grab(host,port):
    s = socket.socket()
    s.settimeout(5)
    s.connect((host,int(port)))
    print(str(s.recv(1024)))

def main():
    host = input("Enter Ip to scan: ")
    port = str(input("Enter the port you want to scan: "))
    try:
        for i in range(1,1024):
            port = i
            portScan(host,port)
    except KeyboardInterrupt:
        exit()
        
    
main()

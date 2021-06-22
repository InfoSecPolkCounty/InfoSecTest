import subprocess,nmap3

def python_subprocess_shell():
    target = input('Enter Target: ')
    portn_num = input('Enter the port Number/s to scan (443,1-6535)')
    nmap = nmap3.Nmap()
    ports = nmap.PortScanner()
    port_scan = ports.scan(target,port_num)
    while True:
        try:
            command = input('Enter command to execute: ')
            subprocess.call(command)
        except KeyboardInterrupt:
            break

python_subprocess_shell()

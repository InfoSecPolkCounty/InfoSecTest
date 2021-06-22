import win32com.client
import os
from datetime import datetime, timedelta
import re
import csv

file_path = 'C:/Users/grayp/Desktop/Attack_Data.txt'
file = open(file_path, 'w')
file_writer = csv.writer(file)
attacks = ["Remote Code Execution","Command Injection","Mozi","Config File Download Attempt","Lokibot","XML External Entity Attack","Malicious Scan Request","ThinkPHP getShell Remote Code Execution","Directory Information Leak","Data Execution Protection","Gpon Router Cmd Injection","Remote OS Command Injection"]
header = ["Ipaddress","Attack"]
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")
for account in mapi.Accounts:
	print(account.DeliveryStore.DisplayName)

inbox = mapi.GetDefaultFolder(6).Folders["syslog"]
messages = inbox.Items
file_writer.writerow(header)
for message in messages:
    body = message.Body
    pattern_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    ips = pattern_ip.findall("Remote Host IP:" + body)
    ip = ips[2]
    for attack in attacks:
        if attack in body:
            parsed_data = [str(ip),str(attack)]
            file_writer.writerow(parsed_data)
        if attack not in body:
                print(message)
file.close()
subprocess.call('taskkill /im outlook.exe')
            


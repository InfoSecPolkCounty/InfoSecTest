import hashlib
import time
filename = input("Enter File location: ")
securehash = input("Enter Expected Hash : ")
with open(filename,"rb") as f:
    bytes = f.read() # read entire file as bytes
    readable_hash = hashlib.sha256(bytes).hexdigest();




try:
    if (str(readable_hash) == securehash):
        print("\n\n[+] File Integrity Secure")
        print(f"File Hash: \t" + str(readable_hash) + "\nSecureHash: \t" + securehash)
    else:
        print("[!] Integrity NOT SECURE")
    time.sleep(45)
        
except KeyboardInterrupt:
    exit()

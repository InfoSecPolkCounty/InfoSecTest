#! usr/bin/env python3
import base64

base64_message = input("Enter the string to decode base64 \n>")
message = str(base64_message)
base64_decoded_message = []

def decode(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)
    base64_decoded_message.append(message)

"""for i in range(0,12):
    decode(base64_message)
    base64_message = base64_decoded_message[i]
    print(i)"""
decode(base64_message)

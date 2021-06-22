import base64

message = input("Enter the string to encode base64 \n>")
message = str(message)
base641_message = []
def encode(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
    base641_message.append(base64_message)


for i in range(0,12):
    encode(message=message)
    message=base641_message[i]
    print(i)

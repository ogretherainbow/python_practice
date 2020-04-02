import socket

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket real good")
except:
    print("socket real bad")

port = 55555
host_ip = "127.0.0.1"
message = "Hello"

client.connect((host_ip, port))
client.send(message.encode())

from_server = client.recv(1024)
print(from_server.decode())

num1 = ""
num2 = ""
i = 0
separate = 0

for char in from_server.decode():
    if char == "*":
        separate = i
    elif char.isdigit():
        if separate == 0:
            num1 = num1 + char
        elif separate > 0:
            num2 = num2 + char
        else:
            print("Error1")
    i = i + 1
answer = str((int(num1) * int(num2)))
print(num1 + " * " + num2 + " equals " + answer)

client.send(answer.encode())
from_server = client.recv(1024)
print(from_server.decode())

client.close()




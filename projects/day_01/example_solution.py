import socket

def main():
    # Create our client object with appropriate socket type and connection information
    client    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server. Note: IPs are passed as strings and ports as ints
    client.connect(('127.0.0.1', 55556))
    # Send the initial "hello" message. In older versions of python, it would auto convert your strings to bytes.
    # You must now do it explicitly. Easy enough to do as a byte string like below,
    # or using the bytes() method as shown later.
    client.send(b"Hello")

    # Grab the response from the server
    from_server = client.recv(1024).decode()
    print(from_server)

    # In one line I am stripping off the ending '?', splitting on spaces, and taking the last 3 parts,
    # and joining them all together in 1 string. You could have also used [-3:]
    equation = "".join(from_server.rstrip('?').split(" ")[2:5])
    # equation = "".join(from_server.rstrip('?').split(" ")[-3:])

    # Making sure my split worked
    # print(from_server.split(" ")[2:5])


    # print(eval(equation))
    # client.send(b'{}'.format(eval(equation)))
    # can't do above: AttributeError: 'bytes' object has no attribute 'format'

    # print(eval(equation))
    # solves equation
    # print(type(eval(equation)))
    # is type int

    answer = str(eval(equation)).encode()
    # The server won't accept type(int), so I encode it into a string.
    # You can do this encoding inside the bytes() call
    # client.send(bytes(str(eval(equation)).encode()))
    client.send(bytes(answer))

    # print the last response
    print(str(client.recv(1024).decode()))

    # Gracefully close the connection
    # Don't leave open sockets. The server SHOULD handle it, but just in case, play nicely
    print("Closing connection")
    client.close()

print("Connection closed...")

if __name__ == '__main__':
    main()

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('', 10000)
sock.bind(server_address)
print('starting up on {} port {}'.format(*sock.getsockname()), file=sys.stderr)
sock.listen(1)

while True:
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address, file=sys.stderr)
        while True:
            data = connection.recv(16)
            print('received "{}"'.format(data), file=sys.stderr)
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()


import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 8838))

s.listen(5) #telling the OS that I am ready to receive requests

connection, address = s.accept()

data = connection.recv(2048)

response = bytes("Hello ".encode("utf-8") + str(data).encode("utf-8") + "!".encode("utf-8"))

connection.sendall(response)

connection.close()

s.close()


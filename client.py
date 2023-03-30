import socket

ip_addr_server = "127.0.0.1"
port = 8838

#1. Create a socket object
s = socket.socket(
    socket.AF_INET, # ipv4
    socket.SOCK_STREAM
)
# socket(IP_Layer_Info,Transport_Layer_Info)
# connect to server -> ip, port, transport layer
# AF -> Address Family
# INET -> IPV4
# SOCK_STREAM -> TCP

#ephermal port
#2. Connect to a server
s.connect(("127.0.0.1",8838))

#3. Send data as Bytes
#a. Convert data into byte[]
#b. while(!complete_data_sent) :
    # send_next_1024_bytes()
# axios.send(file)
# while(True):
#   s.send()
data_to_send = "Hello how are you"

data_to_send_bytes = bytes(data_to_send.encode("utf-8"))

s.sendall(data_to_send_bytes)

# 4. Receive Data
# while(!complete_data_received):
data_received = s.recv(2048)
#   process_those

print(data_received)

# 5. Close Connection
s.close()
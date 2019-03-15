import socket

IP = "10.108.33.5 "
PORT = 8097

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))
except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
ip = s.getsockname()[0]
send_bytes = str.encode(ip)
s.send(send_bytes)

print("Read from the server: ", s.recv(2048).decode("utf-8"))
print("Read from the server: ", s.recv(2048).decode("utf-8"))
print("Read from the server: ", s.recv(2048).decode("utf-8"))

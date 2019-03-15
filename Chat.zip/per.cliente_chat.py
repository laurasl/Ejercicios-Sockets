import socket

IP = "212.128.254.157"
PORT = 9080

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

def process_server(serversocket):
    mensaje = serversocket.recv(1024)
    print (mensaje)

process_server(s)
while True:

    mensaje = input("mensaje: ")
    mensaje_cliente = str.encode(mensaje)
# We must write bytes, not a string
    s.send(mensaje_cliente)
    if mensaje == "Salir":
        break
    process_server(s)

s.close()
print("Read from the server", s.recv(2048).decode("utf-8"))

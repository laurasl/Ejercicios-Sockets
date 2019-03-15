import socket
import threading

PORT = 9080
IP = "212.128.254.157"
MAX_OPEN_REQUESTS = 5

def process_client(clientsocket):
    print(clientsocket)
    msg_bienvenida  = "Bienvenido!"
    send_bytes = str.encode(msg_bienvenida)
    clientsocket.send(send_bytes)
    while True:
         peticion = clientsocket.recv(1024)
         print ("Mensaje recibido:",peticion)
         if peticion == "salir":
             break
         respuesta = input("Respuesta: ")
         respuesta_servidor = str.encode(respuesta)
    # We must write bytes, not a string
         clientsocket.send(respuesta_servidor)
    clientsocket.close()


# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Esperando conexiones en %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)


except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)

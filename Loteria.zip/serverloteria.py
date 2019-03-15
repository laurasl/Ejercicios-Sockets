import socket
import random
import threading

PORT = 8097
IP = "10.108.33.5 "
MAX_OPEN_REQUESTS = 2

def process_client(clientsocket):
    print(clientsocket)
    msg_bienvenida  = "Bienvenido a la lotería. Suerte!"
    send_bytes = str.encode(msg_bienvenida)
    clientsocket.send(send_bytes)
    ip_cliente =  clientsocket.recv(2048).decode("utf-8")
    listaip= ip_cliente.split(".")
    r=random.randrange(0,10)
    for numero in listaip:
        suma=int(listaip[0])+int(listaip[1])+int(listaip[2])+int(listaip[3])
        resto=suma%10
    if resto==r:
        mensaje=('¡Enhorabuena!Te ha tocado. El número era el: ')
        send_bytes = str.encode(mensaje)
        r = str(r)
        send_r = str.encode(r)
            # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.send(send_r)

    else:
        mensaje=('Vaya, esta vez no ha habido suerte. El número era el: ')
        send_bytes = str.encode(mensaje)
        r = str(r)
        send_r = str.encode(r)
            # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.send(send_r)

    clientsocket.close()
# Crear un socket para recibir peticiones
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtener el nombre del servidor, del sistema
hostname = IP

try:
    # Asociar el socket a este servidor y el puerto elegido
    serversocket.bind((hostname, PORT))

    # Configurar el socket: modo servidor
    serversocket.listen(MAX_OPEN_REQUESTS)
    print("Esperando Conexiones en {} {}".format(hostname, PORT))
    (clientsocket, address) = serversocket.accept()
    process_client(clientsocket)


except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)

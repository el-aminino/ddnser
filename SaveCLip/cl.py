import socket


#Define server and port
host = "127.0.0.1"
port = 1381

#using with statement connection will be closed afte body codes done
with socket.socket() as client_socket :
    client_socket.connect((host,port))
    ACK = client_socket.recv(1024).decode()
    if ACK.lower().strip() == "took":
        print("Server Now Knows me !")



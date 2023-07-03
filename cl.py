import socket


#Define server and port
host = "127.0.0.1"
port = 1381
ACK = ""
secret = "secret"

#using with statement connection will be closed afte body codes done
with socket.socket() as client_socket :
    try :
         #client connects to specified host and port
        client_socket.connect((host,port))
        client_socket.send(secret.encode())
        #waits for acknowlege from server
        ACK = client_socket.recv(1024).decode()
        
        
        #checks for 'took' in acknowlege
        if ACK.lower().strip() == "took":
            print("Server Now Knows me !")
    except :
        print("server is down or something else is wrong")

        



import socket

#Define port and bining ip
host = "127.0.0.1"
port = 1381

ACK = "took"
fail = "failed"

#Using with statement which closes the connection when done
with socket.socket() as server_socket :




    server_socket.bind((host,port)) #server is up on specified port
    server_socket.listen() #waits for any request


    #creates a connection and also keeps connection datas
    conn , addr = server_socket.accept()

    client_ip = addr[0] #find client ip address and save it into a variable

    #checks if client's  IP saved or not
    if client_ip :
        conn.send(ACK.encode())
    else:
        conn.send(fail.encode())
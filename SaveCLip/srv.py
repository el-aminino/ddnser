import socket

#Define port and bining ip
host = "127.0.0.1"
port = 1381

ACK = "took"
fail = "failed"

#Using with statement which closes the connection when done
while True :
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket :



        server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR,1)
        server_socket.bind((host,port)) #server is up on specified port
        server_socket.listen(1024) #waits for any request


        #creates a connection and also keeps connection datas
        conn , addr = server_socket.accept()

        client_ip = addr[0] #find client ip address and save it into a variable
        print("")
        print("------------------")
        print("something recieved")
        print("------------------")
        print("")
        #checks if client's  IP saved or not
        if client_ip :
            conn.send(ACK.encode())

            with open("ips" , 'r') as file:
                contents = file.readlines()
                if client_ip+"\n" not in contents : 
                    with open("ips",'a') as appendfile :
                        appendfile.write(client_ip)
                        appendfile.write("\n")
                else :
                    print("IP already exist!")
                    print("Update performed")




        else:
            conn.send(fail.encode())
        
    #server_socket.shutdown(socket.SHUT_RD)    
    server_socket.close()
    server_socket = None

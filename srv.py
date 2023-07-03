import socket
import dns.query
import dns.tsigkeyring
import dns.update
import dns.message
import dns.rdatatype


#Errors and acknowlegements
ACK = "t"
false_secret = "FS"
fail = "f"

#server definition
host = "127.0.0.1"
port = 1381
zone = "test.com"


#secret
secret = "secret"

#to check if client IP is in specified zone
def check_zone(zone,server,recieved_ip):
    query = dns.message.make_query(zone, dns.rdatatype.ANY)
    response = str(dns.query.tcp(query,server))
 
    
    if recieved_ip in response:
        return True
    else:
        return False
    


while True:
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as srv_socket :


        #this kills all of the TCP connections and free ups specified port 
        srv_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR ,1)

        #starts server on specified por
        srv_socket.bind((host,port))

        #waits for client to send message
        srv_socket.listen()

        #creates and connection from connection maked
        conn , addr = srv_socket.accept()

        #takes client secret
        queez = conn.recv(1024).decode()
        


        #checks that secrets are the same
        if queez == secret :

            #saves IP of client
            client_ip = addr[0]

            #checks if client IP saved Completely
            if client_ip:
                #sends acknowledgement to client
                conn.send(ACK.encode())

                print("------------------")
                print("Something Recieved")
                print("------------------")
                
                #checks if client IP exsist in zone and server or not

                is_in_zone = check_zone(zone, host, client_ip)

                if is_in_zone :
                    print("Record exits")
                else:
                    print("Record not not exist")





            else:
                #sends fail to client
                srv_socket.send(fail.encode())

        else: 
            #lets client know that secret is false
            srv_socket.send(false_secret.encode())

        




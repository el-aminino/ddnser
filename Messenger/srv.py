import socket

def srvprg() :
    host = "127.0.0.1"
    port = 1381
    srv_socket = socket.socket()
    srv_socket.bind((host,port))
    srv_socket.listen(10)
    
    conn , address = srv_socket.accept()
    print("Connection from =" + str(address))
    while True:
        
    
        data = conn.recv(1024).decode()
        if not data :
            break
        print("connect user" + str(data))
        data = input("  ->  ")
        conn.send(data.encode())
        
    
    conn.close()








if __name__ == '__main__':
    srvprg()
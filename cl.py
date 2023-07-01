import socket

def clprog():
    host = "192.168.1.23"
    port = 1381
    cl_socket = socket.socket()
    cl_socket.connect((host,port))
    message = input("   ->  ")
    while message.lower().strip() != "bye!":
        cl_socket.send(message.encode())
        data = cl_socket.recv(1024).decode()
        print("recieved message is :" + data)
        message = input("   ->  ")
        cl_socket.close()

    



if __name__ == '__main__':
    clprog()
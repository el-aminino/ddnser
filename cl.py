import socket

def clinet():
    host = "127.0.0.1"
    port = 1381


    cli_sct = socket.socket()
    cli_sct.connect((host,port))
    
    message=input("   ->   ")

    while message.lower().strip() != "bye":
        cli_sct.send(message.encode())
        data = cli_sct.recv(1024).decode()
        print("Here is what is recieved: "+ str(data) )
        message = input("   ->   ")
    
    cli_sct.close()

if __name__ == '__main__':
    clinet()
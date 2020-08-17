import socket #std library
import time

sA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HEADERSIZE = 10

#binding socket
sA.bind((socket.gethostname(), 5000)) #bind to a port
sA.listen(5) #listening for information

#server side logic
while True:
    clientsocket, adress = sA.accept()
    sB.connect((socket.gethostname(), 9000))
    print(f"Server had connected to {adress} successfully!")
    """
    msg = "Welcome to the server!"
    header_with_msg = f'{len(msg):<{HEADERSIZE}}' + msg
    
    clientsocket.send(bytes(header_with_msg, "utf-8"))
    """

#client side logic
"""
while True:
    decoded_msg = ''
    new_msg = True
    while True:
        msg = s.recv(50)
        if new_msg:
            print("Incomming message length: ", msg[:HEADERSIZE])
            message_length = int(msg[:HEADERSIZE])
            new_msg = False

        decoded_msg += msg.decode("utf-8")
        
        if len(decoded_msg)-HEADERSIZE == message_length:
            print("Full Message received")
            print(decoded_msg[HEADERSIZE:])
            new_msg = True
"""
import socket
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
sB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sB.connect(('192.168.0.129', 5000))
import socket
import threading
import time

sA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting socket
sB.connect((socket.gethostname(), 9000))

#binding socket
sA.bind((socket.gethostname(), 5000)) #bind to a port
sA.listen(5) #listening for information

#server side logic
clientsocket, adress = sA.accept()
print(f"Server had connected to {adress} successfully!")

def sending():
    while True:
        user = input(r'')
        clientsocket.send(bytes(user, "utf-8"))
        continue

def receiving():
    while True:
        msg = sB.recv(2048)
        decode = msg.decode("utf-8")
        print(decode)
        continue

t1 = threading.Thread(target=sending)
t2 = threading.Thread(target=receiving)

t1.start()
t2.start()
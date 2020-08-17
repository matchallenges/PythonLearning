import socket # std library
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5000))
s.listen(5)

while True:
    clientsocket, adress = s.accept()
    print(f"Server had connected to {adress} successfully!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<10} + msg'
    #msg = '{:<10}'.format('Welcome to the server')


    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()
"""

msg = "Welcome to the server!"
print(f'{msg}')
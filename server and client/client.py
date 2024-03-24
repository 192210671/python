import socket

c=socket.socket()

c.connect(('localhost',10061))


name=input("Enter the name:")

c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())

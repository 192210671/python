import socket

s = socket.socket()

s.bind(('localhost', 9999))

s.listen(3)
print("Waiting For Connections")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()

    print("Connected With:", addr,name)

    c.send(bytes("Welcome to This Page", 'utf-8'))

    c.close()

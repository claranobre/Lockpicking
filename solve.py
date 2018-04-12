from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)

sock.connect(("127.0.0.1",1337))
print('connectou!')
print(sock.recv(2048).decode())
x = input("Digite a senha: ")
sock.send(x.encode('ascii'))
print(sock.recv(2048).decode())
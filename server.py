import socket
import sys
import string
import threading

_bufsize = 4096

def clientThread(client):
    msg = '''
                    +++    JerimumHackerspace - LockHack | By: @claranobre & @K4L1   +++

 Digite a senha! :)
 
 Para começar, digite start:'''
                        
    client.send(msg.encode())
    userStart = client.recv(_bufsize).strip().decode('ascii')
    
    if 'teste' == userStart:
        client.send(' Parabens! Agora digite no keypad!\n'.encode())
    else:
        client.send(' Tente novamente\n'.encode())
    client.close()


bind_ip = "0.0.0.0"
bind_port = int(sys.argv[1])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print ("[*] ouvindo no", bind_ip, bind_port)

while(1):
	client, addr = server.accept()
	print("[*] Novo cliente:", addr[0], addr[1])

	#tratamento de dados:
	client_handler = threading.Thread(target=clientThread, args=(client,))
	if(client_handler == 1):
		continue
	client_handler.start()
server.close()
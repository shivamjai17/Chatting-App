import socket
import sys
a='BYE'
def new_func(server_socket):
    client_socket,client_addr=server_socket.accept()
    return client_socket,client_addr

if len(sys.argv)==3:
    try:
        SERVER_IP=sys.argv[1].strip().lower()
        SERVER_PORT=int(sys.argv[2])
        ADDRESS=(SERVER_IP,SERVER_PORT)
        server_socket=socket.socket()
        server_socket.bind(ADDRESS)
        server_socket.listen()
        print(f"Server is ready to accept Client Request at : {ADDRESS}")
        print()
        client_socket, client_addr = new_func(server_socket)
        print(f"Connected to Client at: {client_addr}")
        print()
        while True:
            cmsg=client_socket.recv(1024).decode()
            print(f"Client msg :{cmsg}".rjust(100))
            if cmsg.upper().strip()==a:
                client_socket.send(a.encode())
                break
            smsg=input("Server msg :").encode()
            client_socket.send(smsg)
            if smsg.decode().upper().strip()==a:
                break
        client_socket.close()    
        server_socket.close()
    except Exception as error:
        print('Usages: server.py server_ip server_port')
        print("ERROR!!",error)
        sys.exit(1)
else:
    print("Usages: server_ip server_port")
    sys.exit(2)            
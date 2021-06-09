import sys
import socket
a='BYE'
if len(sys.argv)==3:
    try:
        SERVER_IP=sys.argv[1]
        SERVER_PORT=int(sys.argv[2])
        ADDRESS=(SERVER_IP,SERVER_PORT)
        client_socket=socket.socket()
        client_socket.connect(ADDRESS)
        print(f"Successfully Connect to SERVER at :{ADDRESS}")
        while True:
            csmg=input("Client : ").encode()
            client_socket.send(csmg)
            if csmg.decode().upper().strip()==a:
                break
            smsg=client_socket.recv(1024).decode()
            if smsg.upper().strip()==a:
                break
            print(f"Server : {smsg}".rjust(100))
        client_socket.close()
    except Exception as error:
        print("Usages: client.py SERVER_IP SERVER_PORT")
        print("ERROR!!",error)
        sys.exit(1)    
else:
    print("Usage: Client.py SERVER_IP SERVER_PORT")
    sys.exit(2)        
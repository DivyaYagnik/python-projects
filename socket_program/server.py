import socket 
import threading

# max length in bytes of incoming message
# used to handle differing lengths of messages
HEADER = 64
# character encoding
FORMAT = 'utf-8'
PORT = 5050
# print this message to disconnect from server
DISCONNECT_MSG = "DISCONNECT"
# local IP address
SERVER = socket.gethostbyname(socket.gethostname())
# uniquely identfies type of connection and communication
ADDR = (SERVER, PORT)

# initialise socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to address
server.bind(ADDR)

def handle_client(conn, addr):
    # print(f"[NEW CONNECTION] {user.name} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message received".encode(FORMAT))

    conn.close()

def start():
    # listen for connections
    server.listen()
    print(f"[LISTENING] Server is listening on address {SERVER}")
    while True: 
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} ")


print("[STARTING] server is starting...")
start()
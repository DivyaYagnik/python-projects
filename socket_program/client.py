import socket 
from .server import handle_client

HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
DISCONNECT_MSG = "!DISCONNECT!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

class User:
    def __init__(self, name):
        self.name = name

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

isname = 0
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

message_valid = True

username = input("Enter your name: ")
user = User(username)
name_message = f"[NEW CONNECTION] {user.name} connected"
send(name_message)

while message_valid:
    msg = input("Enter message: ")
    if msg == DISCONNECT_MSG:
        message_valid = False
    send(msg)
import threading # From standard library
import socket # From standard library

host = '127.0.0.1' # Localhost
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clients = {}

# Broadcast messages received from connected clients
def broadcast():
    pass


# Receive messages from clients to be broadcasted
def handle():
    pass


# Receive clients to the server
def receive():
    pass



if __name__ == '__main__':
    print('The server is listening...')
    pass

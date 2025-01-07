from datetime import datetime
import threading
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12352    # Port to listen on (non-privileged port)

DISCONNECT_MESSAGE = '/exit'
JOINED_MESSAGE = 'JOINED_MESSAGE'
RECV_SIZE = 1024

clients = {}    # Tracking all the clients in the chat

# Broadcast messages received from connected clients
def broadcast(message):
    message = f'[{str(datetime.now())[:18]}] {message}' # Padding the message
    for client in clients.keys():
        client.send(message.encode('ascii'))


# Allowing a user to exit the server
def server_exit(client):
    broadcast(f'{clients[client]} has left the chat!'.encode('ascii'))
    del clients[client]
    client.close()


# Receive messages from clients to be broadcasted
def handle(client):
    while True:
        try:
            message = client.recv(RECV_SIZE).decode('ascii')
            if message.lower() == DISCONNECT_MESSAGE:
                server_exit(client)
                break
            elif message.upper() == JOINED_MESSAGE:
                client.send('Invalid Message!'.encode('ascii'))
                break
            else:
                broadcast(f'{clients[client]}: {message}')
        except:
            client.send('Invalid Message! Too many characters'.encode('ascii'))
            break


# Receive clients to the server
def receive():
    while True:
        # Connecting the client and logging the joining information
        client, address = server.accept()
        print(f'User connected with {str(address)} at {datetime.now()}')

        # To get nickname from the client
        client.send('JOINED_MESSAGE'.encode('ascii'))

        try:
            nickname = client.recv(RECV_SIZE).decode('ascii')
            clients[client] = nickname
            
            # Logging nickname
            print(f'Nickname of the client is {nickname}')

            # Broadcasting the nickname
            broadcast(f'{nickname} has joined the chat!')
            client.send(f'Connected to the server as {nickname}'.encode('ascii'))
            
            # Creating a client specific process thread for the client
            thread = threading.Thread(target=handle, args=(client, ))
            thread.start()
            print(f'Total Active Connections: {len(clients)}')

        except:
            print('Invalid Nickname! Too many characters')
            server_exit(client)



if __name__ == '__main__':
    # Initializing the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f'Server initialized at {datetime.now()}')
    print('The server is now listening...')
    receive()

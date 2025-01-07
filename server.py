from datetime import datetime
import threading
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12345    # Port to listen on (non-privileged port)

DISCONNECT_MESSAGE = '/exit'
RECV_SIZE = 1024

# Broadcast messages received from connected clients
def broadcast(message:str):
    message = datetime.now() + ': ' + message # Padding the message
    for client in clients.key():
        client.send(message)


# Allowing a user to exit the server
def server_exit(client):
    broadcast(f'{clients[client]} has left the chat!'.encode('ascii'))
    del clients[client]
    client.close()


# Receive messages from clients to be broadcasted
def handle(client):
    while True:
        try:
            message = client.recv(RECV_SIZE)
            if message.lower() == DISCONNECT_MESSAGE:
                server_exit(client)
                break
            else:
                broadcast(message)
        except:
            print('Invalid Message! Too many characters')
            break


# Receive clients to the server
def receive():
    while True:
        # Connecting the client and logging the joining information
        client, address = server.accept()
        print(f'User connected with {str(address)} at {datetime.now()}')

        # To get nickname from the client
        client.send('NICKNAME'.encode('ascii'))

        try:
            nickname = client.recv(RECV_SIZE).decode('ascii')
            clients[client] = nickname
            
            # Logging nickname
            print(f'Nickname of the client is {nickname}')

            # Broadcasting the nickname
            broadcast(f'{nickname} has joined the chat!'.encode('ascii'))
            client.send(f'Connect to the server as {nickname}'.encode('ascii'))
            
            # Creating a client specific process thread for the client
            thread = threading.Thread(target=handle, args=(client, ))
            thread.start()

        except:
            print('Invalid Nickname! Too many characters')
            server_exit(client)



if __name__ == '__main__':
    # Initializing the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    clients = {}    # Tracking all the clients in the chat

    print(f'Server initialized at {datetime.now()}')
    print('The server is now listening...')
    receive()

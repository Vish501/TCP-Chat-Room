from datetime import datetime # From standard library
import threading # From standard library
import socket # From standard library

host = '127.0.0.1' # Localhost
port = 12345

# Initializing the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = {}

# Broadcast messages received from connected clients
def broadcast(message:str):
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
            message = client.recv(1024)
            if message.lower() == '--exit':
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
            nickname = client.recv(1024).decode('ascii')
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
    print(f'Server initialized at {datetime.now()}')
    print('The server is now listening...')
    receive()

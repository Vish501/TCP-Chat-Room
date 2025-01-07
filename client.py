from datetime import datetime
import threading
import socket

RECV_SIZE = 1024
JOINED_MESSAGE = 'JOINED_MESSAGE'

# Connecting to the client
def receive():
    while True:
        try:
            message = client.recv().decode('ascii')
            if message == JOINED_MESSAGE:
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('An error occured! Closing Connection...')
            client.close()
            break


# Writing a message to be broadcasted by the server
def write_messsage():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))



if __name__ == '__main__':
    host = input(f'Enter the host you want to connect to: ')
    port = int(input(f'Enter the port you want to connect to: '))
    nickname = input(f'Enter the nickname you want to use: ')

    print('Trying to initialize connection...')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((host, port))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write_messsage)
    write_thread.start()

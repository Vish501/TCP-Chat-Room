from datetime import datetime
import threading
import socket


# Connecting to the client
def receive():
    pass


# Writing a message to be broadcasted by the server
def write_messsage():
    pass



if __name__ == '__main__':
    host = input(f'Enter the host you want to connect to: ')
    port = int(input(f'Enter the port you want to connect to: '))

    print('Trying to initialize connection...')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((host, port))

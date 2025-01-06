import threading # From standard library
import socket # From standard library

host = input(f'Enter the host you want to connect to: ')
port = int(input(f'Enter the port you want to connect to: '))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connecting to the client
def receive():
    pass


# Writing a message to be broadcasted by the server
def write_messsage():
    pass



if __name__ == '__main__':
    print('Initializing Connection...')
    pass

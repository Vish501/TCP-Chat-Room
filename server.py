import threading # From standard library
import socket # From standard library

host = '127.0.0.1' # Localhost
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#!/usr/bin/python3

import SocketUtils as su
from threading import Thread as thr

class ChatServer():

    def __init__(self, port = 5000):
        '''initializes new chat server'''
        self.clients = {}  # initializing clients dictionary
        self.addresses = {}  # initializing client addresses dictionary

        self.host = ''  # all available interfaces
        self.port = port  # assigning port, default is 5000
        self.sock = (self.host, port)

        self.server = su.sck.socket(su.sck.AF_INET, su.sck.SOCK_STREAM)  # initalize socket
        self.server.bind(self.sock)  # attach to socket

    def broadcast(self, message, prefix = ""):
        '''broadcast a message to all online clients'''

        for sock in self.clients:
            sock.sendall(bytes(prefix + message, "utf-8"))

    def handle_client(self, client_sock):
        '''allows client to chat'''

        ok = 0
        while ok == 0:
            client_sock.sendall(bytes("Choose your name: ", "utf-8"))
            client_name = client_sock.recv(su.maxBuffSize).decode("utf-8")
            ok = su.confirm(client_sock)

        client_name = client_name[:len(client_name)]
        self.clients[client_sock] = client_name

        message = "Welcome, " + client_name + "! Quit by typing \"!exit\"."
        client_sock.sendall(bytes(message, "utf-8"))

        message = client_name + " has joined the chat! Give him a warm welcome!\r\n"
        self.broadcast(message)  # announce the new client

        while True:
            # receive new message from client
            message = client_sock.recv(su.maxBuffSize).decode("utf-8")
            print(client_name + " has sent the message: " + message)

            if message[: len(message)] != "!exit":
                self.broadcast(message, client_name + ": ")

            else:  # if the client wants to exit
                # exit = su.confirm(client_sock)
                if exit == 0:
                    continue

                client_sock.sendall(bytes("Exiting...", "utf-8"))
                client_sock.close()
                del self.clients[client_sock]

                self.broadcast(" has left the chat.\n", client_name + ": ")
                break

    def accept_connection(self):
        '''allows entrance for incoming clients'''

        while True:
            client, client_addr = self.server.accept()  # accept connection
            self.addresses[client] = client_addr  # adding to client dictionary

            print(client_addr, "has connected to the server.")
            client.sendall(bytes("Welcome to the Chat!", "utf-8"))

            # starting a new thread specific to client
            thr(target = self.handle_client, args = (client, )).start()

if __name__ == "__main__":
    server = ChatServer(port = 2399)
    server.server.listen(5)
    thrd = thr(target = server.accept_connection)
    thrd.start()
    thrd.join()
    server.server.close()

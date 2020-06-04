#!/usr/bin/python3

import SocketUtils as su
from threading import Thread as thr
import tkinter as tk

class ChatClient():

    def __init__(self):
        '''initializes the client thread and socket'''
        self.server = input("Enter host: ")
        self.port = int(input("Enter port: "))

        self.sock = su.sck.socket(su.sck.AF_INET, su.sck.SOCK_STREAM)
        self.sock.connect((self.server, self.port))

    def receiveMessage(self):
        '''enables client to receive message from server'''
        while True:
            try:
                message = self.sock.recv(su.maxBuffSize).decode("utf-8")
                self.messagesBox.insert(tk.END, message)

            except OSError:
                break

    def sendMessage(self, event = None):
        '''sends message from client's input'''
        message = self.myMessage.get()
        self.myMessage.set("")  # empty input box after the message is sent

        self.sock.sendall(bytes(message, "utf-8"))
        if message == "!exit":
            self.sock.close()
            self.top.quit()

    def exitChat(self, event = None):
        '''function called when the client exits the chat'''
        self.myMessage.set("!exit")
        self.sendMessage()
        print("Closing the window...")

    def initChatGUI(self):
        '''initializes the chat's GUI'''
        self.top = tk.Tk()  # initialize Chat Top Bar
        self.top.title("Chat Room")  # Give it a title

        self.chatFrame = tk.Frame(self.top)  # assign the top bar with a Frame
        self.scrollbar = tk.Scrollbar(self.chatFrame)  # initalize a Scrollbar

        self.myMessage = tk.StringVar()  # initialize input box
        self.myMessage.set("")

        self.messagesBox = tk.Listbox(self.chatFrame, height = 30, width = 50,
                            yscrollcommand = self.scrollbar.set)

        # placing everything in the right places
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        self.messagesBox.pack(side = tk.LEFT, fill = tk.BOTH)
        self.messagesBox.pack()
        self.chatFrame.pack()

        # initializing input box
        self.inputBox = tk.Entry(self.top, textvariable = self.myMessage)
        self.inputBox.bind("<Return>", self.sendMessage)
        self.inputBox.pack()

        # initializing the send button
        self.sendButton = tk.Button(self.top, text = "Send",
                            command = self.sendMessage)
        self.sendButton.pack()

        # assign exit procedure
        self.top.protocol("WM_DELETE_WINDOW", self.exitChat)

if __name__ == "__main__":
    client = ChatClient()
    client.initChatGUI()

    # initialize client Thread
    receiveThread = thr(target = client.receiveMessage)
    receiveThread.start()

    tk.mainloop()

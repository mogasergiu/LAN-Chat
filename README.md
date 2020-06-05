# LAN-Chat
  A Chat Application with a simple GUI, which can be used to communicate across a LAN on a shared group. It can also
be used in WAN's but that would require a better suited host with a public IP address for the Server Application to
be run on.

  In order to start the program, "ServerUtils.py" must be run on a terminal instance on one of the hosts. By default,
the Server listens on the port 2399 and can take up to 10 connected clients (these can be easily modified in the
Source Code). The Client application can also use the Port Scanner implementes in SocketUtils.py to dinamically
discover the port the Server is actually listening on, in case it has been changed.

  To start chatting, simply run the "ClientUtils.py" in a terminal instance and a Chat Window will appear prompting the
client for a desired username, after which he will be enabled to chat with other clients connected to the same Server.
Unlike the Server Application, the Client Application has a GUI. The Server may can also log all connected hosts and
their chats.

Modules used:
- tkinter: for the Client side GUI
- sys: only used for the sys.exit() method
- threading: used by the Server Application to handle multiple connections and by the Client Application to be able to
             communicate in a full duplex manner
- sockets: the module used the most, enables the programmability of the network and hosts' intercommunication using the
           TCP protocol
             
Future Plans:
- Make the GUI more appealing/colorful
- Implement Separate Chat Rooms
- Enable users to share images

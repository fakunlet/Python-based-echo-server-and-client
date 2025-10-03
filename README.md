# Python-based-echo-server-and-client
A simple Python-based echo server and client using the socket library to demonstrate TCP (reliable) and UDP (unreliable) communication at the transport layer

Requirements:
Python 3

Files:
server.py: The echo server.
client.py: The client that sends a message.

How to Run:
Open two terminals.
In the first: python server.py 
In the second: python client.py 

Example Output:

Server output:
TCP Echo Server started on localhost:8888
Waiting for connections... (Press Ctrl+C to stop)
Connection established with ('127.0.0.1', 54321)
Received from ('127.0.0.1', 54321): Hello, Server!
Echoed back to ('127.0.0.1', 54321): Hello, Server!

Client output:
Connecting to localhost:8888...
Connected to server at localhost:8888
Type messages to send to server (type 'quit' to exit)
> Hello, Server!
Server echoed: Hello, Server!
> quit
Disconnected from server

UDP Variation:
For UDP, modify the code to use SOCK_DGRAM and adjust send/receive methods (no connect/accept).

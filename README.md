# Python-based-echo-server-and-client
A simple Python-based echo server and client using the socket library to demonstrate TCP (reliable) and UDP (unreliable) communication at the transport layer

Requirements:
Python 3

Files:
server.py: The echo server.
client.py: The client that sends a message.

How to Run:
Open two terminals.
In the first: python server.py (listens on localhost:12345).
In the second: python client.py (sends "Hello, Echo Server!" and prints the echo).

UDP Variation:
For UDP, modify the code to use SOCK_DGRAM and adjust send/receive methods (no connect/accept).

#!/usr/bin/env python3
"""
Simple TCP Echo Client
Connects to the echo server and sends messages to test the echo functionality.
"""

import socket
import sys
import threading

def receive_messages(client_socket):
    """Receive and display messages from server"""
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print("Server disconnected")
                break
            message = data.decode('utf-8')
            print(f"Server echoed: {message}")
    except ConnectionResetError:
        print("Server disconnected")
    except Exception as e:
        print(f"Error receiving messages: {e}")

def start_client(host='localhost', port=8888):
    """Start the TCP echo client"""
    try:
        # Create socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to server
        print(f"Connecting to {host}:{port}...")
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        print("Type messages to send to server (type 'quit' to exit)")
        
        # Start thread to receive messages
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()
        
        # Send messages
        while True:
            message = input("> ")
            if message.lower() == 'quit':
                break
            
            # Send message to server
            client_socket.send(message.encode('utf-8'))
            
    except ConnectionRefusedError:
        print(f"Could not connect to {host}:{port}. Make sure the server is running.")
    except KeyboardInterrupt:
        print("\nDisconnecting...")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        try:
            client_socket.close()
            print("Disconnected from server")
        except:
            pass

if __name__ == "__main__":
    # Allow custom host and port via command line arguments
    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8888
    
    start_client(host, port)


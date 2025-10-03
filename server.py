#!/usr/bin/env python3
"""
Simple TCP Echo Server
Listens for incoming connections and echoes back any data received.
"""

import socket
import sys
import threading

def handle_client(client_socket, client_address):
    """Handle individual client connections"""
    print(f"Connection established with {client_address}")
    
    try:
        while True:
            # Receive data from client
            data = client_socket.recv(1024)
            if not data:
                print(f"Client {client_address} disconnected")
                break
            
            # Decode and display received message
            message = data.decode('utf-8')
            print(f"Received from {client_address}: {message}")
            
            # Echo the message back to client
            client_socket.send(data)
            print(f"Echoed back to {client_address}: {message}")
            
    except ConnectionResetError:
        print(f"Client {client_address} disconnected unexpectedly")
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"Connection with {client_address} closed")

def start_server(host='localhost', port=8888):
    """Start the TCP echo server"""
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow socket reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Bind to host and port
        server_socket.bind((host, port))
        print(f"TCP Echo Server started on {host}:{port}")
        print("Waiting for connections... (Press Ctrl+C to stop)")
        
        # Listen for connections
        server_socket.listen(5)
        
        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            
            # Handle client in a separate thread
            client_thread = threading.Thread(
                target=handle_client, 
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
        print("Server stopped")

if __name__ == "__main__":
    # Allow custom host and port via command line arguments
    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8888
    
    start_server(host, port)


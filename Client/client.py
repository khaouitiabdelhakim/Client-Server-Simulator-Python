import socket
import webbrowser


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 12345

client_socket.connect((host, port))



while True:
    message = input("search: ")
    if message.lower() == "quit":
        break
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()

    # Create a temporary HTML file
    with open('temp.html', 'w') as f:
        f.write(response)

    # Open the temporary HTML file in the default web browser
    webbrowser.open('temp.html')

client_socket.close()    

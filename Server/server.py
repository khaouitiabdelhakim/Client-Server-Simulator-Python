import socket


html = """
<!DOCTYPE html>
<html>
<head>
    <title>Googlo - Your Ultimate Browser</title>
</head>
<body>
    <h1>Welcome to Googlo!</h1>
    <p>Your ultimate browser experience starts here.</p>
</body>
</html>
"""

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 12345

    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening on", host, "port", port)

    while True:
        print("Waiting for a client to connect...")
        client_socket, client_address = server_socket.accept()
        print("Connected to:", client_address)

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            browser_name = data.lower()

            if browser_name == "googlo":
                response = html
            else:
                response = "Sorry, we could'n find what you search"

            client_socket.send(response.encode())

        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    main()

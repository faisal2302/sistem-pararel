import socket
import threading

clients = {}  # simpan socket dan username client

# Mengirim pesan ke semua client
def broadcast(message, _client_socket=None):
    for client_socket in clients:
        if client_socket != _client_socket:
            try:
                client_socket.send(message)
            except:
                client_socket.close()
                if client_socket in clients:
                    del clients[client_socket]

# Menangani setiap client
def handle_client(client_socket, address):
    try:
        username = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = username
        print(f"[+] {username} ({address}) terhubung.")
        broadcast(f"[SERVER]: {username} bergabung ke chat!\n".encode('utf-8'))

        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            full_message = f"[{username}]: {message.decode('utf-8')}\n"
            print(full_message.strip())
            broadcast(full_message.encode('utf-8'), client_socket)

    except:
        pass
    finally:
        if client_socket in clients:
            left_user = clients[client_socket]
            print(f"[-] {left_user} terputus.")
            broadcast(f"[SERVER]: {left_user} keluar dari chat.\n".encode('utf-8'))
            del clients[client_socket]
            client_socket.close()

# Menjalankan server
def start_server():
    host = '127.0.0.1'
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[SERVER] Berjalan di {host}:{port}")

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    start_server()
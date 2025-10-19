import socket
import threading

# Menerima pesan dari server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message, end="")
        except:
            print("\nKoneksi ke server terputus.")
            client_socket.close()
            break

# Menjalankan client
def start_client():
    host = '127.0.0.1'
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except:
        print("Gagal terhubung ke server.")
        return

    username = input("Masukkan username Anda: ")
    client_socket.send(username.encode('utf-8'))
    print(f"Terhubung ke server sebagai '{username}'. Ketik pesan Anda (atau 'exit' untuk keluar):\n")

    # Thread untuk menerima pesan
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input("")
        if message.lower() == 'exit':
            print("Menutup koneksi...")
            client_socket.close()
            break
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            print("Koneksi terputus.")
            break

if __name__ == "__main__":
    start_client()
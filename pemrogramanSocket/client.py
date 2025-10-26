import socket

# Menentukan alamat server dan port yang sama
host = '127.0.0.1'
port = 5000

# Membuat socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Terhubung ke server
    client.connect((host, port))
    print(f"[CLIENT] Terhubung ke server {host}:{port}")

    while True:
        message = input("Ketik pesan (atau 'exit' untuk keluar): ")
        if message.lower() == 'exit':
            break

        # Mengirim pesan ke server
        client.send(message.encode('utf-8'))

        # Menerima balasan dari server
        reply = client.recv(1024).decode('utf-8')
        print(f"[BALASAN SERVER]: {reply}")

except ConnectionRefusedError:
    print("Gagal terhubung ke server. Pastikan server sudah berjalan.")
finally:
    # Menutup koneksi client
    client.close()
    print("[CLIENT] Koneksi ditutup.")

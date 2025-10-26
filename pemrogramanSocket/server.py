import socket

# Menentukan alamat dan port server
host = '127.0.0.1'  # localhost
port = 5000

# Membuat socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print(f"[SERVER] Menunggu koneksi di {host}:{port} ...")

# Menerima koneksi dari client
conn, addr = server.accept()
print(f"[TERHUBUNG] Koneksi dari {addr}")

while True:
    # Menerima pesan dari client
    data = conn.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"[PESAN DARI CLIENT]: {data}")

    # Mengirim balasan ke client
    reply = "Pesan telah diterima oleh server."
    conn.send(reply.encode('utf-8'))

# Menutup koneksi
conn.close()
server.close()
print("[SERVER] Koneksi ditutup.")

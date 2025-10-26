import socket

# setting IP dan port
host = '127.0.0.1'
port = 5000

# membuat socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print("Server sedang berjalan di", host, "port", port)
print("Menunggu client terhubung...")

# terima koneksi dari client
conn, addr = server.accept()
print("Terhubung dengan:", addr)

# terima pesan dari client
data = conn.recv(1024).decode()
print("Pesan dari client:", data)

# kirim balasan ke client
balasan = "Server sudah menerima pesan kamu."
conn.send(balasan.encode())

# tutup koneksi
conn.close()
server.close()

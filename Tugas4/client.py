import socket

# alamat IP server dan port harus sama dengan server.py
host = '127.0.0.1'
port = 5000

# membuat socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# kirim pesan ke server
pesan = input("Masukkan pesan untuk server: ")
client.send(pesan.encode())

# terima balasan dari server
data = client.recv(1024).decode()
print("Balasan dari server:", data)

# tutup koneksi
client.close()

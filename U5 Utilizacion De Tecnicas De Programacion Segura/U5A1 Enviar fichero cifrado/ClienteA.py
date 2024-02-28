import socket

# Dirección y puerto del servidor (ClienteB)
SERVER_ADDRESS = ('localhost', 12345)

# Lee el archivo cifrado
with open("archivo_cifrado.txt", "rb") as f:
    data = f.read()

# Inicia la conexión con el servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(SERVER_ADDRESS)
    sock.sendall(data)
    print("Archivo enviado a ClienteB")

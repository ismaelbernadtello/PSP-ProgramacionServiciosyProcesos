import socket

# Dirección y puerto del servidor (ClienteB)
SERVER_ADDRESS = ('localhost', 12345)

# Inicia el servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(SERVER_ADDRESS)
    sock.listen(1)
    print("Esperando conexión...")

    conn, addr = sock.accept()

    with conn:
        print('Conectado por', addr)
        data = conn.recv(1024)
        with open("archivo_recibido.txt", "wb") as f:
            f.write(data)
        print("Archivo recibido de ClienteA")
